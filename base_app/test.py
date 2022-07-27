def TLdashboard(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            return redirect('/')

        user_id = user_registration.objects.get(id=tlid)
        conf_sal = user_id.confirm_salary
        if conf_sal == "":
            conf_sal = 0
        else:
            conf_sal = int(user_id.confirm_salary)

        last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
        start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)

        start_day_of_this_month = date.today().replace(day=1)

        def last_day_of_month(any_day):
            # get close to the end of the month for any day, and add 4 days 'over'
            next_month = any_day.replace(day=28) + timedelta(days=4)
            # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
            return next_month - timedelta(days=next_month.day)

        last_day_of_this_month = last_day_of_month(date.today())

        previous_sal_main = 0
        this_month_sal_main = 0

        if conf_sal > 0:
            

            last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
            start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)


            prev_holly_day = Event.objects.filter(start_time__range=(start_day_of_prev_month,last_day_of_prev_month)).count()

            # print("Previous Month Holly day:", prev_holly_day)
            working_days_pre = ((last_day_of_prev_month - start_day_of_prev_month).days - prev_holly_day) + 1
            # print("Previous Month working days:", working_days_pre)
            one_day_sal_pre = round((conf_sal / working_days_pre), 2)
            # print("Previous Month one day salary:", one_day_sal_pre)

            # print("First day of prev month:", start_day_of_prev_month)
            # print("Last day of prev month:", last_day_of_prev_month)


            pre_current = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month), submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')
            pre_start_current = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= tlid).values('startdate','enddate','submitted_date')
            pre_start_current_sub_other = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(~Q(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(developer_id= tlid).values('startdate','enddate','submitted_date')
            pre_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(enddate__range=(start_day_of_prev_month,last_day_of_prev_month), submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')
            pre_start_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= tlid).values('startdate','enddate','submitted_date')

            
            pre_this_month_have_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month)), ~Q(enddate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= tlid).values('submitted_date')
            pre_this_month_have_not_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month)), ~Q(enddate__range=(start_day_of_prev_month,last_day_of_prev_month)),submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')



            prev_current_delay = 0
            prev_current_delay = 0
            print("TL From date and to date are in previous month it does not have submission date  :", pre_current.count())
            for pre_current in pre_current:
                end_date =  (pre_current['enddate'])
                holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
                delay_days = (last_day_of_prev_month - end_date).days
                work_days = delay_days - holy

                prev_current_delay = prev_current_delay +  work_days

        

            print("TL From date and to date are in previous month it does have submission date :", pre_start_current.count())
            for pre_start_current in pre_start_current:
                end_date =  (pre_start_current['enddate'])
                submitted_date =  (pre_start_current['submitted_date'])

                if submitted_date <= end_date:
                    work_days = 0
                    prev_current_delay = prev_current_delay +  work_days
                else:
                    holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                    delay_days = (submitted_date - end_date).days
                    work_days = delay_days - holy
                    
                    prev_current_delay = prev_current_delay +  work_days

            print("TL Start and End date seleted month it does have submission date other month :", pre_start_current_sub_other.count())
            for pre_start_current_sub_other in pre_start_current_sub_other:
                end_date =  (pre_start_current_sub_other['enddate'])
                submission_date = (pre_start_current_sub_other['submitted_date'])
                if submission_date is not None:
                    if last_day_of_prev_month < submission_date:

                        holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
                        delay_days = (last_day_of_prev_month - end_date).days
                        work_days = delay_days - holy

                        prev_current_delay = prev_current_delay +  work_days

            print("TL End date previous month it does not have submission date  :", pre_current_sub.count())
            for pre_current_sub in pre_current_sub:
                end_date =  (pre_current_sub['enddate'])
                holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
                delay_days = (last_day_of_prev_month - end_date).days
                work_days = delay_days - holy

                prev_current_delay = prev_current_delay +  work_days

                
                
            print("TL End date previous month it have submission date is previous month :", pre_start_current_sub.count())
            for pre_start_current_sub in pre_start_current_sub:
                end_date =  (pre_start_current_sub['enddate'])
                submitted_date =  (pre_start_current_sub['submitted_date'])

                if submitted_date <= end_date:
                    work_days = 0
                    prev_current_delay = prev_current_delay +  work_days
                else:
                    holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                    delay_days = (submitted_date - end_date).days
                    work_days = delay_days - holy

                    prev_current_delay = prev_current_delay +  work_days

                


            print("TL End date and start date not in previous month but submission date in previous month :", pre_this_month_have_submission.count())
            for pre_this_month_have_submission in pre_this_month_have_submission:
                submitted_date =  (pre_this_month_have_submission['submitted_date'])
                if start_day_of_prev_month <= submitted_date:

                    holy = Event.objects.filter(start_time__range=(start_day_of_prev_month,submitted_date )).count()
                    delay_days = (submitted_date - start_day_of_prev_month).days + 1
                    work_days = delay_days - holy

                    prev_current_delay = prev_current_delay + work_days


        


            print("TL From date and to date are not in previous month it does not have submission date :", pre_this_month_have_not_submission.count())
            for pre_this_month_have_not_submission in pre_this_month_have_not_submission:
                end_date = (pre_this_month_have_not_submission['enddate'])

                if end_date <= last_day_of_prev_month:

                    holy = Event.objects.filter(start_time__range=(start_day_of_prev_month,last_day_of_prev_month)).count()
                    delay_days = (last_day_of_prev_month - start_day_of_prev_month).days  + 1
                    work_days = delay_days - holy

                    prev_current_delay = prev_current_delay + work_days

            previous_sal_main
            print("prev_current_delay", prev_current_delay)
            delay_sal_previous = round((one_day_sal_pre * prev_current_delay), 2)
            print("Delay salary Cut previous month", delay_sal_previous)
            previous_sal_main = round((conf_sal - delay_sal_previous), 2)
            print("Previous month total salary",previous_sal_main)

            if previous_sal_main <= 0:
                previous_sal_main = 0


           

            start_day_of_this_month = date.today().replace(day=1)

            def last_day_of_month(any_day):
                # get close to the end of the month for any day, and add 4 days 'over'
                next_month = any_day.replace(day=28) + timedelta(days=4)
                # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
                return next_month - timedelta(days=next_month.day)

            last_day_of_this_month = last_day_of_month(date.today())
            # print("First day of This  month:", start_day_of_this_month)
            # print("Last day of This month:", last_day_of_this_month)

            holly_day_current = Event.objects.filter(start_time__range=(start_day_of_this_month,last_day_of_this_month)).count()
            # print("Holly day:", holly_day_current)
            working_days_current = ((last_day_of_this_month - start_day_of_this_month).days - holly_day_current) + 1
            # print("Current Month day:", working_days_current)
            one_day_sal_current = round((conf_sal / working_days_current), 2)
            # print("One Day:", one_day_sal_current)

            This_month_leave_count = leave.objects.filter(from_date__gte = start_day_of_this_month, to_date__lte = date.today(), user_id = tlid).count()
            This_month_leave_count_sub = leave.objects.filter(from_date__range=(start_day_of_this_month,date.today()),to_date__range=(start_day_of_this_month,date.today()), user_id = tlid).values('from_date','to_date')
            this_month_leave = 0
            this_month_leave_in_work = 0

            if This_month_leave_count >= 1:

                for This_month_leave_count_sub in This_month_leave_count_sub:

                    from_date = (This_month_leave_count_sub['from_date'])
                    to_date =  (This_month_leave_count_sub['to_date'])

                    tot_hollyday = Event.objects.filter(start_time__range=(from_date,to_date)).count()
                    days_leave = (to_date - from_date).days
                    if days_leave >= 1:
                        days_leave = days_leave + 1
                    tot_days = days_leave - tot_hollyday
                    this_month_leave = this_month_leave + tot_days

            print("This month leave count", this_month_leave )


            pro_current = project_taskassign.objects.filter(startdate__range=(start_day_of_this_month,date.today()),enddate__range=(start_day_of_this_month,date.today()), submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')
            pro_start_current = project_taskassign.objects.filter(startdate__range=(start_day_of_this_month,date.today()),enddate__range=(start_day_of_this_month,date.today())).filter(submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= tlid).values('startdate','enddate','submitted_date')
            pro_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today()))).filter(enddate__range=(start_day_of_this_month,date.today()), submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')
            pro_start_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today()))).filter(enddate__range=(start_day_of_this_month,date.today()),submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= tlid).values('startdate','enddate','submitted_date')

            
            pro_this_month_have_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today())), ~Q(enddate__range=(start_day_of_this_month,date.today())),submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= tlid).values('submitted_date')
            pro_this_month_have_not_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today())), ~Q(enddate__range=(start_day_of_this_month,date.today())),submitted_date__isnull = True).filter(developer_id= tlid).values('startdate','enddate')

            yes_current = 0
            print("From date and to date are in this month it does not have submission date  :", pro_current.count())
            for pro_current in pro_current:
                end_date =  (pro_current['enddate'])
                holy = Event.objects.filter(start_time__range=(end_date,date.today())).count()
                delay_days = (date.today() - end_date).days
                work_days = delay_days - holy

                yes_current = yes_current +  work_days



            print("From date and to date are in this month it does have submission date :", pro_start_current.count())
            for pro_start_current in pro_start_current:
                end_date =  (pro_start_current['enddate'])
                submitted_date =  (pro_start_current['submitted_date'])
                if submitted_date <= end_date:
                    work_days = 0
                    yes_current = yes_current + work_days
                else:
                    holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                    delay_days = (submitted_date - end_date).days
                    work_days = delay_days - holy

                    yes_current = yes_current + work_days



  
            print("End date this month it does not have submission date  :", pro_current_sub.count())
            for pro_current_sub in pro_current_sub:
                end_date =  (pro_current_sub['enddate'])
                holy = Event.objects.filter(start_time__range=(end_date,date.today())).count()
                delay_days = (date.today() - end_date).days
                work_days = delay_days - holy

                yes_current = yes_current +  work_days

                


           
                
            print("End date this month it have submission date :", pro_start_current_sub.count())
            for pro_start_current_sub in pro_start_current_sub:
                end_date =  (pro_start_current_sub['enddate'])
                submitted_date =  (pro_start_current_sub['submitted_date'])

                if submitted_date <= end_date:
                    work_days = 0
                    yes_current = yes_current + work_days
                else:

                    holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                    delay_days = (submitted_date - end_date).days
                    work_days = delay_days - holy

                    yes_current = yes_current + work_days




            print("End date and start date not in this month but  submission date in this :", pro_this_month_have_submission.count())
            for pro_this_month_have_submission in pro_this_month_have_submission:

            
                submitted_date =  (pro_this_month_have_submission['submitted_date'])
                holy = Event.objects.filter(start_time__range=(start_day_of_this_month,submitted_date )).count()
                delay_days = (submitted_date - start_day_of_this_month).days + 1
                work_days = delay_days - holy

                yes_current = yes_current + work_days





            print("From date and to date are not in this month it does not have submission date :", pro_this_month_have_not_submission.count())
            for pro_this_month_have_not_submission in pro_this_month_have_not_submission:
                end_date = (pro_this_month_have_not_submission['enddate'])

                if end_date <= date.today():

                    holy = Event.objects.filter(start_time__range=(start_day_of_this_month,date.today())).count()
                    delay_days = (date.today() - start_day_of_this_month).days + 1
                    work_days = delay_days - holy

                    yes_current = yes_current + work_days


    



            print("This month work in leave count", this_month_leave_in_work)
            print("Current Month Delay", yes_current)
            delay_sal_current = round((one_day_sal_current * yes_current), 2)
            print("Delay salary Cut", delay_sal_current)
            this_month_sal_main = round((conf_sal - delay_sal_current), 2)
            print("This month total salary",this_month_sal_main)

            if this_month_sal_main <= 0:
                this_month_sal_main = 0

            
        else:
            previous_sal_main = 0
            this_month_sal_main = 0







        mem = user_registration.objects.filter(id=tlid)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=tlid)
        dev = user_registration.objects.filter(tl_id=tlid)
        ids = dev.values_list('id', flat="true")
        des = designation.objects.get(designation="developer")
        le = leave.objects.filter(user_id__in=ids.all(
        ), designation_id=des.id, leaveapprovedstatus=0)

        

        for i in queryset:
            labels = [i.workperformance, i.attitude, i.creativity]
            data = [i.workperformance, i.attitude, i.creativity]
        return render(request, 'TLdashboard.html', {'labels': labels, 'data': data, 'mem': mem, 'le': le,
         'previous_sal_main':previous_sal_main, 'this_month_sal_main':this_month_sal_main, 'last_day_of_prev_month':last_day_of_prev_month, 'start_day_of_prev_month':start_day_of_prev_month })
    else:
        return redirect('/')



def devdashboard(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
       return redirect('/')
    


    user_id = user_registration.objects.get(id=devid)
    conf_sal = user_id.confirm_salary
    if conf_sal == "":
        conf_sal = 0
    else:
        conf_sal = int(user_id.confirm_salary)

    last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
    start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)

    start_day_of_this_month = date.today().replace(day=1)

    def last_day_of_month(any_day):
        # get close to the end of the month for any day, and add 4 days 'over'
        next_month = any_day.replace(day=28) + timedelta(days=4)
        # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
        return next_month - timedelta(days=next_month.day)

    last_day_of_this_month = last_day_of_month(date.today())

    previous_sal_main = 0
    this_month_sal_main = 0

    if conf_sal > 0:
        

        


        prev_holly_day = Event.objects.filter(start_time__range=(start_day_of_prev_month,last_day_of_prev_month)).count()

        # print("Previous Month Holly day:", prev_holly_day)
        working_days_pre = ((last_day_of_prev_month - start_day_of_prev_month).days - prev_holly_day) + 1
        # print("Previous Month working days:", working_days_pre)
        one_day_sal_pre = round((conf_sal / working_days_pre), 2)
        # print("Previous Month one day salary:", one_day_sal_pre)

        # print("First day of prev month:", start_day_of_prev_month)
        # print("Last day of prev month:", last_day_of_prev_month)


        pre_current = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month), submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')
        pre_start_current = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= devid).values('startdate','enddate','submitted_date')
        pre_start_current_sub_other = project_taskassign.objects.filter(startdate__range=(start_day_of_prev_month,last_day_of_prev_month),enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(~Q(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(developer_id= devid).values('startdate','enddate','submitted_date')
        pre_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(enddate__range=(start_day_of_prev_month,last_day_of_prev_month), submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')
        pre_start_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(enddate__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= devid).values('startdate','enddate','submitted_date')

        
        pre_this_month_have_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month)), ~Q(enddate__range=(start_day_of_prev_month,last_day_of_prev_month))).filter(submitted_date__range=(start_day_of_prev_month,last_day_of_prev_month)).filter(developer_id= devid).values('submitted_date')
        pre_this_month_have_not_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_prev_month,last_day_of_prev_month)), ~Q(enddate__range=(start_day_of_prev_month,last_day_of_prev_month)),submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')



        pre_month_leave_count = Event.objects.filter(start_time__gte = "2022-05-01", start_time__lte = "2022-05-27").count()   
        print("pre hollyday in gte lte", pre_month_leave_count)
        pre_month_leave_count_sub = Event.objects.filter(start_time__range=("2022-05-01", "2022-05-27")).count()
        print("pre hollyday in range", pre_month_leave_count_sub)    


        prev_current_delay = 0
        print("dev From date and to date are in previous month it does not have submission date  :", pre_current.count())
        for pre_current in pre_current:
            end_date =  (pre_current['enddate'])
            holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
            delay_days = (last_day_of_prev_month - end_date).days
            work_days = delay_days - holy

            prev_current_delay = prev_current_delay +  work_days


        print("dev From date and to date are in previous month it does have submission date :", pre_start_current.count())
        for pre_start_current in pre_start_current:
            end_date =  (pre_start_current['enddate'])
            submitted_date =  (pre_start_current['submitted_date'])

            delay_days = (submitted_date - end_date).days
            if delay_days <= 0:
                work_days = 0
                prev_current_delay = prev_current_delay +  work_days
            else:
                delay_days = (submitted_date - end_date).days
                holy = Event.objects.filter(start_time__gte=end_date,start_time__lte = submitted_date).count()
                work_days = delay_days - holy
                prev_current_delay = prev_current_delay +  work_days
                
        
        print("dev Start and End date seleted month it does have submission date other month :", pre_start_current_sub_other.count())
        for pre_start_current_sub_other in pre_start_current_sub_other:
            end_date =  (pre_start_current_sub_other['enddate'])
            submission_date = (pre_start_current_sub_other['submitted_date'])
            if submission_date is not None:
                if last_day_of_prev_month < submission_date:

                    holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
                    delay_days = (last_day_of_prev_month - end_date).days
                    work_days = delay_days - holy

                    prev_current_delay = prev_current_delay +  work_days

        print("dev End date previous month it does not have submission date  :", pre_current_sub.count())
        for pre_current_sub in pre_current_sub:
            end_date =  (pre_current_sub['enddate'])
            holy = Event.objects.filter(start_time__range=(end_date,last_day_of_prev_month)).count()
            delay_days = (last_day_of_prev_month - end_date).days
            work_days = delay_days - holy

            prev_current_delay = prev_current_delay +  work_days

            
            
        print("dev End date previous month it have submission date is previous month :", pre_start_current_sub.count())
        for pre_start_current_sub in pre_start_current_sub:
            end_date =  (pre_start_current_sub['enddate'])
            submitted_date =  (pre_start_current_sub['submitted_date'])

            if submitted_date <= end_date:
                work_days = 0
                prev_current_delay = prev_current_delay +  work_days
            else:
                holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                delay_days = (submitted_date - end_date).days
                work_days = delay_days - holy

                prev_current_delay = prev_current_delay +  work_days

            


        print("dev End date and start date not in previous month but submission date in previous month :", pre_this_month_have_submission.count())
        for pre_this_month_have_submission in pre_this_month_have_submission:
            submitted_date =  (pre_this_month_have_submission['submitted_date'])
            if start_day_of_prev_month <= submitted_date:

                holy = Event.objects.filter(start_time__range=(start_day_of_prev_month,submitted_date )).count()
                delay_days = (submitted_date - start_day_of_prev_month).days + 1
                work_days = delay_days - holy

                prev_current_delay = prev_current_delay + work_days


    


        print("dev From date and to date are not in previous month it does not have submission date :", pre_this_month_have_not_submission.count())
        for pre_this_month_have_not_submission in pre_this_month_have_not_submission:
            end_date = (pre_this_month_have_not_submission['enddate'])

            if end_date <= last_day_of_prev_month:

                holy = Event.objects.filter(start_time__range=(start_day_of_prev_month,last_day_of_prev_month)).count()
                delay_days = (last_day_of_prev_month - start_day_of_prev_month).days  + 1
                work_days = delay_days - holy

                prev_current_delay = prev_current_delay + work_days


        previous_sal_main
        print("prev_current_delay", prev_current_delay)
        delay_sal_previous = one_day_sal_pre * prev_current_delay
        print("Delay salary Cut previous month", delay_sal_previous)
        previous_sal_main = round((conf_sal - delay_sal_previous), 2)
        print("Previous month total salary",previous_sal_main)

        if previous_sal_main <= 0:
            previous_sal_main = 0


        

        
        # print("First day of This  month:", start_day_of_this_month)
        # print("Last day of This month:", last_day_of_this_month)

        holly_day_current = Event.objects.filter(start_time__range=(start_day_of_this_month,last_day_of_this_month)).count()
        # print("Holly day:", holly_day_current)
        working_days_current = ((last_day_of_this_month - start_day_of_this_month).days - holly_day_current) + 1
        # print("Current Month day:", working_days_current)
        one_day_sal_current = round((conf_sal / working_days_current), 2)
        # print("One Day:", one_day_sal_current)

        tot_day = 0
        work_del = 0
        this_month_leave = leave.objects.filter(from_date__range=(start_day_of_this_month,date.today()),to_date__range=(start_day_of_this_month,date.today()), user_id  = devid).values('from_date','to_date')

        for x in this_month_leave:
            from_date = x['from_date']
            to_date = x['to_date']
            diff_days = ((to_date - from_date).days ) + 1
            if diff_days == 0:
                main_days = 0
                tot_day = tot_day + main_days
            else:
                hol= Event.objects.filter(start_time__gte=from_date,start_time__lte=to_date).count()
                main_days = (diff_days - hol)
                tot_day = tot_day + main_days

        print("This month Leave",tot_day )

        def delay_leave_ext(start,end):
            this_month_leave = leave.objects.filter(from_date__range=(start_day_of_this_month,date.today()),to_date__range=(start_day_of_this_month,date.today()), user_id  = devid).values('from_date','to_date')

            for x in this_month_leave:
                from_date = x['from_date']
                to_date = x['to_date']
                diff_days = ((to_date - from_date).days ) + 1
                if diff_days == 0:
                    main_days = 0
                    tot_day = tot_day + main_days
                else:
                    hol= Event.objects.filter(start_time__gte=from_date,start_time__lte=to_date).count()
                    main_days = (diff_days - hol)
                    tot_day = tot_day + main_days



        pro_current = project_taskassign.objects.filter(startdate__range=(start_day_of_this_month,date.today()),enddate__range=(start_day_of_this_month,date.today()), submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')
        pro_start_current = project_taskassign.objects.filter(startdate__range=(start_day_of_this_month,date.today()),enddate__range=(start_day_of_this_month,date.today())).filter(submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= devid).values('startdate','enddate','submitted_date')
        pro_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today()))).filter(enddate__range=(start_day_of_this_month,date.today()), submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')
        pro_start_current_sub = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today()))).filter(enddate__range=(start_day_of_this_month,date.today()),submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= devid).values('startdate','enddate','submitted_date')

        
        pro_this_month_have_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today())), ~Q(enddate__range=(start_day_of_this_month,date.today())),submitted_date__range=(start_day_of_this_month,date.today())).filter(developer_id= devid).values('submitted_date')
        pro_this_month_have_not_submission = project_taskassign.objects.filter(~Q(startdate__range=(start_day_of_this_month,date.today())), ~Q(enddate__range=(start_day_of_this_month,date.today())),submitted_date__isnull = True).filter(developer_id= devid).values('startdate','enddate')

        yes_current = 0
        print("dev From date and to date are in this month it does not have submission date  :", pro_current.count())
        for pro_current in pro_current:
            end_date =  (pro_current['enddate'])
            holy = Event.objects.filter(start_time__range=(end_date,date.today())).count()
            delay_days = (date.today() - end_date).days
            work_days = delay_days - holy

            yes_current = yes_current +  work_days


        print("dev From date and to date are in this month it does have submission date :", pro_start_current.count())
        for pro_start_current in pro_start_current:
            end_date =  (pro_start_current['enddate'])
            submitted_date =  (pro_start_current['submitted_date'])
            if submitted_date <= end_date:
                work_days = 0
                yes_current = yes_current + work_days
            else:
                holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                delay_days = (submitted_date - end_date).days
                work_days = delay_days - holy

                yes_current = yes_current + work_days


    

        print("dev End date this month it does not have submission date  :", pro_current_sub.count())
        for pro_current_sub in pro_current_sub:
            end_date =  (pro_current_sub['enddate'])
            holy = Event.objects.filter(start_time__range=(end_date,date.today())).count()
            delay_days = (date.today() - end_date).days
            work_days = delay_days - holy

            yes_current = yes_current +  work_days

          
        

        
            
        print("dev End date this month it have submission date :", pro_start_current_sub.count())
        for pro_start_current_sub in pro_start_current_sub:
            end_date =  (pro_start_current_sub['enddate'])
            submitted_date =  (pro_start_current_sub['submitted_date'])

            if submitted_date <= end_date:
                work_days = 0
                yes_current = yes_current + work_days
            else:

                holy = Event.objects.filter(start_time__range=(end_date,submitted_date)).count()
                delay_days = (submitted_date - end_date).days
                work_days = delay_days - holy

                yes_current = yes_current + work_days

         


        print("dev End date and start date not in this month but submission date in this :", pro_this_month_have_submission.count())
        for pro_this_month_have_submission in pro_this_month_have_submission:
            
            if start_day_of_this_month <= submitted_date:
                submitted_date =  (pro_this_month_have_submission['submitted_date'])
                holy = Event.objects.filter(start_time__range=(submitted_date,start_day_of_this_month)).count()
                delay_days = (submitted_date - start_day_of_this_month ).days + 1
                work_days = delay_days - holy

                yes_current = yes_current + work_days


        


        print("dev From date and to date are not in this month it does not have submission date :", pro_this_month_have_not_submission.count())
        for pro_this_month_have_not_submission in pro_this_month_have_not_submission:
            end_date = (pro_this_month_have_not_submission['enddate'])

            if end_date <= date.today():

                holy = Event.objects.filter(start_time__range=(start_day_of_this_month,date.today())).count()
                delay_days = (date.today() - start_day_of_this_month).days + 1
                work_days = delay_days - holy

                yes_current = yes_current + work_days


        print("Current Month Delay", yes_current)
        delay_sal_current = round((one_day_sal_current * yes_current), 2)
        print("Delay salary Cut", delay_sal_current)
        this_month_sal_main = round((conf_sal - delay_sal_current), 2)
        print("This month total salary",this_month_sal_main)

        if this_month_sal_main <= 0:
            this_month_sal_main = 0

        
    else:
        previous_sal_main = 0
        this_month_sal_main = 0



    dev = user_registration.objects.filter(id=devid)
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=devid)
    for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
    return render(request, 'devdashboard.html', {'labels':labels,'data':data,'dev': dev,  'previous_sal_main':previous_sal_main, 'this_month_sal_main':this_month_sal_main, 'last_day_of_prev_month':last_day_of_prev_month, 'start_day_of_prev_month':start_day_of_prev_month})

