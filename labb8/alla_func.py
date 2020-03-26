#-- ADT --
def start_time(ts):
    "span -> time"
    ensure(ts, is_time_span)
    return strip_tag(ts)[0]


def end_time(ts):
    "span -> time"
    ensure(ts, is_time_span)
    return strip_tag(ts)[1]


def overlap(ts1, ts2):
    "span x span -> span"
    ensure(ts1, is_time_span)
    ensure(ts2, is_time_span)
    st1 = start_time(ts1)
    st2 = start_time(ts2)
    int_st1 = get_integer(get_hour(st1)) * 60 + get_integer(get_minute(st1))
    int_st2 = get_integer(get_hour(st2)) * 60 + get_integer(get_minute(st2))
    if int_st1 >= int_st2:
        actual_start_time = st1
    else:
        actual_start_time = st2

    et1 = end_time(ts1)
    et2 = end_time(ts2)
    int_et1 = get_integer(get_hour(et1)) * 60 + get_integer(get_minute(et1))
    int_et2 = get_integer(get_hour(et2)) * 60 + get_integer(get_minute(et2))
    if int_et1 <= int_et2:
        actual_end_time = et1
    else:
        actual_end_time = et2

    return new_time_span(actual_start_time, actual_end_time)


def new_duration(hour, minute):
    "hour x minute -> duration"
    overflow_hour = get_integer(minute) // 60
    m = new_minute(get_integer(minute) % 60)
    h = new_hour(get_integer(hour) + overflow_hour)
    return attach_tag("duration", (h, m))


def length_of_span(ts):
    "span -> duration"
    st_h = get_integer(get_hour(start_time(ts)))
    st_m = get_integer(get_minute(start_time(ts)))
    et_h = get_integer(get_hour(end_time(ts)))
    et_m = get_integer(get_minute(end_time(ts)))

    new_h = et_h - st_h
    new_m = et_m - st_m

    if new_m < 0:
        new_m = 60 + new_m
        new_h -= 1

    return new_duration(new_hour(new_h), new_minute(new_m))


def new_time_spans():
    """ -> time_spans """
    return attach_tag("time_spans", [])


def insert_span(time_spans, time_span):
    """ time_span -> time_spans """
    ensure(time_span, is_time_span)

    time_spans = strip_tag(time_spans)
    time_span_inserted = False

    if len(time_spans) == 0:
        time_span_inserted = True
        time_spans.append(time_span)
    else:
        for i in range(len(time_spans)):
            if start_time(time_spans[i]) > start_time(time_span):
                time_spans.insert(i, time_span)
                time_span_inserted = True
                break

    if not time_span_inserted:
        time_spans.append(time_span)

    return attach_tag("time_spans", time_spans)


def is_time_spans(time_spans):
    """ time_spans -> Bool """
    return get_tag(time_spans) == "time_spans"


def get_time_span(time_spans, i):
    """ time_spans x Integer -> time_span """
    return time_spans[1][i]


def is_empty_time_spans(time_spans):
    """ time_spans -> Bool """
    return len(time_spans[1]) == 0


def first_time_span(time_spans):
    """ time_spans -> time_span """
    return time_spans[1][0]


def rest_time_spans(time_spans):
    """ time_spans -> time_spans """
    return attach_tag("time_spans", time_spans[1][1:])


def free_spans(cal_day, start, end):
    """ calendar_day x time x time -> time_spans """
    def find_free_times(st, calendar_day, free_times):
        if st == end: #start and end cant be the same
            return free_times

        if precedes(end, st):
            #hanterar om det finns ett appointment som sträcker sig över end
            return free_times
        elif is_empty_calendar_day(calendar_day):
            #Om det inte finns några appointments kvar, fritt fram till end
            return insert_span(free_times, new_time_span(st, end))
        elif precedes(end, start_time(get_span(\
                first_appointment(calendar_day)))):
            #Hanterar om det finns appointments efter end, men ledig under end
            return insert_span(free_times, new_time_span(st, end))
        elif precedes(st, \
                      start_time(get_span(first_appointment(calendar_day)))):
            #Standard satsen typ, skapar alla time_span mellan appointments
            et = start_time(get_span(first_appointment(calendar_day)))
            new_free_times = insert_span(free_times, new_time_span(st, et))
            temp = find_free_times(end_time(get_span(first_appointment(calendar_day))), rest_calendar_day(calendar_day), new_free_times)
            return temp
        else:
            #kommer aldrig hit förhoppningsvis
            return find_free_times(end_time(get_span(first_appointment(calendar_day))),rest_calendar_day(calendar_day), free_times)

    ft = new_time_spans()

    #if there are no appointments in the cal_day
    if is_empty_calendar_day(cal_day):
            return insert_span(new_time_spans(), new_time_span(start, end))

    def find_first_free_time(calendar_day):
        if is_empty_calendar_day(calendar_day):
            return start

        elif precedes(start, start_time(get_span(first_appointment(calendar_day)))):
            return start
        elif precedes(start, end_time(get_span(first_appointment(calendar_day)))):
            return end_time(get_span(first_appointment(calendar_day)))
        return find_first_free_time(rest_calendar_day(calendar_day))

    first_free_time = find_first_free_time(cal_day)
    new_ft = find_free_times(first_free_time, cal_day, ft)

    return new_ft


def remove_appointment(st, cal_day):
    """ time x calendar_day -> calendar_day """
    def del_app(st, cal_day):
        if not strip_tag(cal_day):
            return []
        if start_time(get_span(first_appointment(cal_day))) == st:
            return del_app(st, rest_calendar_day(cal_day))
        else:
            return [first_appointment(cal_day)] + \
                del_app(st, rest_calendar_day(cal_day))

    return attach_tag("calendar_day", del_app(st, cal_day))



#-- Booking --

def cancel_appointment(cal_year, day, mon, time):
    """ calendar_year x day x month x time -> calendar_year """
    cal_day = calendar_day(day, calendar_month(mon, cal_year))
    return insert_calendar_month(
               mon,
               insert_calendar_day(
                   day,
                   remove_appointment(time, cal_day),
                   calendar_month(mon, cal_year)),
               cal_year)

#-- Calendar --

def remove(cal_name, d, m, time):
    """ string x day x month x time -> """
    day = new_day(d)
    mon = new_month(m)
    start = convert_time(time)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))

    if is_booked_from(cal_day, start):
        insert_calendar(cal_name, cancel_appointment(fetch_calendar(cal_name),
                                                     day, mon, start))
        print ("Appointment removed.")
    else:
        print ("There is no appointment at that time.")


def show_free(cal_name, day, mon, start, end):
    """ String x day x month x time x time -> """
    day = new_day(day)
    mon = new_month(mon)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))
    st = convert_time(start)
    et = convert_time(end)
    show_free_spans(cal_day, st, et)


#-- output --

def show_time_spans(ts):
    """ time_span -> """
    for time_span in ts[1]:
        show_span(time_span)
        print('')


def show_free_spans(cal_day, start_time, end_time):
    """ calendar_day x time x time -> """
    show_time_spans(free_spans(cal_day, start_time, end_time))
