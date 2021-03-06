# =========================================================================
#  Calendar - Functional and imperative programming in Python
#
#  Module: calendar_ADT.py
#  Updated: 2005-09-27 by Peter Dalenius
#    Translated to Python in 2012 by Peter L-G
#    Translated to English in 2013 by Anders M.L.
#  Dependencies:
#    None
# =========================================================================

# This module contains the primitives required for using the abstract data
# types provided in the calendar. It also contains some useful low-level
# functions which operate directly on these.

## =========================================================================
##  1. Basic functions for attaching tags, and ensuring correctness.
## =========================================================================

def attach_tag(type, object):
    "calendar type tag x Python object -> calendar object"
    return (type, object)

def strip_tag(object):
    "calendar object -> Python object"
    if isinstance(object, tuple):
        return object[1]

def get_tag(object):
    "calendar object -> calendar type tag" 
    if isinstance(object, tuple):
        return object[0]

def ensure(val, pred):
    "Arbitrary type a x (a -> Bool) ->"
    assert pred(val), "Value {0} does not conform to type specification.".format(val)

## =========================================================================
##  2. Simple types
## =========================================================================

# ----- HOUR -----
def new_hour(h):
    "Integer -> hour"
    ensure(h, lambda h: isinstance(h, int) and 0 <= h)
    return attach_tag('hour', h)

def is_hour(object):
    "Python object -> Bool"
    return get_tag(object) == 'hour'

# See also: get_integer (under DAY).

# ----- MINUTE -----
def new_minute(m):
    "Integer -> minute"
    ensure(m, lambda m: isinstance(m, int) and 0 <= m)
    return attach_tag('minute', m)

def is_minute(object):
    "Python object -> Bool"
    return get_tag(object) == 'minute'

def get_integer(hour_minute):
    "hour U minute -> Integer"
    ensure(hour_minute, lambda x: is_hour(x) or is_minute(x))
    return strip_tag(hour_minute)


# ----- DAY  -----
def new_day(d):
    "Integer -> day"
    ensure(d, lambda d: isinstance(d, int) and 1 <= d <= 31)
    return attach_tag('day', d)

def is_day(object):
    "Python object -> Bool"
    return get_tag(object) == 'day'

def day_number(day):
    "day -> Integer"
    ensure(day, is_day)
    return strip_tag(day)


# ----- MONTH -----
MONTH_NAMES = {'jan': 'january',
              'feb': 'february',
              'mar': 'march',
              'apr': 'april',
              'may': 'may',
              'jun': 'june',
              'jul': 'july',
              'aug': 'august',
              'sep': 'september',
              'oct': 'october',
              'nov': 'november',
              'dec': 'december'}

MONTH_DAYS = {'january': 31,
              'february': 28,
              'march': 31,
              'april': 30,
              'may': 31,
              'june': 30,
              'july': 31,
              'august': 31,
              'september': 30,
              'october': 31,
              'november': 30,
              'december': 31}

MONTH_NUMBERS = {'january': 1,
                'february': 2,
                'march': 3,
                'april': 4,
                'may': 5,
                'june': 6,
                'july': 7,
                'august': 8,
                'september': 9,
                'october': 10,
                'november': 11,
                'december': 12}
                


def new_month(mon):
    "String -> month"
    if mon in MONTH_DAYS:
        return attach_tag('month', mon)
    else:
        if mon in MONTH_NAMES:
            return attach_tag('month', MONTH_NAMES[mon])
        else:
            raise Exception('\'{0}\' is not a month.'.format(mon))

ALL_MONTHS = [new_month(m_name) for m_name in MONTH_NUMBERS]
            
def is_month(object):
    "Python object -> Bool"
    return get_tag(object) == 'month'

def month_name(mon):
    "month -> String"
    ensure(mon, is_month)
    return strip_tag(mon)

def month_number(mon):
    "month -> Integer"
    ensure(mon, is_month)
    return MONTH_NUMBERS[strip_tag(mon)]

def number_of_days(mon):
    "month -> Integer"
    ensure(mon, is_month)
    return MONTH_DAYS[strip_tag(mon)]


# ----- SUBJECT -----
def new_subject(text):
    "String -> subject"
    ensure(text, lambda t: isinstance(t, str))
    return attach_tag('subject', text)

def is_subject(object):
    "Python object -> Bool"
    return get_tag(object) == 'subject'

def subject_text(subject):
    "subject -> String"
    ensure(subject, is_subject)
    return strip_tag(subject)

## =========================================================================
##  3. Compound types
## =========================================================================

# ----- DURATION -----

#Uppgift 8A
def new_duration(hour, minute):
    "hour x minute -> duration"
    overflow_hour = get_integer(minute) // 60
    m = new_minute(get_integer(minute) % 60)
    h = new_hour(get_integer(hour) + overflow_hour)
    return attach_tag("duration", (h, m))


def is_duration(object):
    "Python object -> Bool"
    return get_tag(object) == 'duration'

def get_hour(duration_time):
    "duration U time -> hour"
    if is_duration(duration_time):
        return strip_tag(duration_time)[0]
    elif is_time(duration_time):
        return strip_tag(duration_time)[0]
    else:
        raise Exception('Arguments passed to get_hour should be of type duration or time.')

def get_minute(duration_time):
    "duration U time -> minute"
    if is_duration(duration_time):
        return strip_tag(duration_time)[1]
    elif is_time(duration_time):
        return strip_tag(duration_time)[1]
    else:
        raise Exception('Arguments passed to get_minute should be of type duration or time.')


# ----- TIME -----
def new_time(hour, minute):
    "hour x minute -> time"
    ensure(hour, is_hour)
    ensure(minute, is_minute)
    if get_integer(hour) > 23:
        raise Exception('The hour {0} does not conform to type specification.'.format(hour))
    elif get_integer(minute) > 59:
        raise Exception('The minute {0} does not conform to type specification.'.format(minute))
    else:
        return attach_tag('time', (hour, minute))

def is_time(object):
    "Python-object -> Bool"
    return get_tag(object) == 'time'


# ----- SPAN -----
def new_time_span(t1, t2):
    "time x time -> span"
    ensure(t1, is_time)
    ensure(t2, is_time)
    if is_same_time(t1, t2):
        raise Exception('Start and end time are the same, {0}, {1}.'.format(t1, t2))
    elif not precedes(t1, t2):
        raise Exception('Start time {0} cannot succeed the end time {1}.'.format(t1, t2))
    else:
        return attach_tag('span', (t1, t2))

def is_time_span(object):
    "Python-object -> Bool"
    return get_tag(object) == 'span'

# start_time should be re-written (7A).
def start_time(ts):
    "span -> time"
    ensure(ts, is_time_span)
    return strip_tag(ts)[0]

# end_time is to be re-written (7A).
def end_time(ts):
    "span -> time"
    ensure(ts, is_time_span)
    return strip_tag(ts)[1]


#----- DATE -----
def new_date(day, mon):
    "day x month -> date"
    ensure(day, is_day)
    ensure(mon, is_month)
    if day_number(day) > number_of_days(mon):
        raise Exception('Date {0}, {1} does not conform to specifications.'.format(day, mon))
    else:
        return attach_tag('date', (mon, day))

def is_date(object):
    "Python-object -> Bool"
    return get_tag(object) == 'date'

def get_month(date):
    "date -> month"
    ensure(date, is_date)
    return strip_tag(date)[0]

def get_day(date):
    "date -> day"
    ensure(date, is_date)
    return strip_tag(date)[1]


# ----- APPOINTMENT -----
def new_appointment(per, subject):
    "span x subject -> appointment"
    ensure(per, is_time_span)
    ensure(subject, is_subject)
    return attach_tag('appointment', (per, subject))

def is_appointment(object):
    "Python-object -> Bool"
    return get_tag(object) == 'appointment'

def get_span(app):
    "appointment -> tidsperiod"
    ensure(app, is_appointment)
    return strip_tag(app)[0]

def get_subject(app):
    "appointment -> subject"
    ensure(app, is_appointment)
    return strip_tag(app)[1]


# ----- CALENDAR_DAY -----
def new_calendar_day():
    " -> calendar_day"
    return attach_tag('calendar_day', [])

def is_calendar_day(object):
    "Python-object -> Bool"
    return get_tag(object) == 'calendar_day'

def is_empty_calendar_day(cal_day):
    "calendar_day -> Bool"
    ensure(cal_day, is_calendar_day)
    return not strip_tag(cal_day)

def insert_appointment(app, cal_day):
    "appointment x calendar_day -> calendar_day"

    def add_appointment(al, app):
        if not al or precedes(start_time(get_span(app)),
                              start_time(get_span(al[0]))):
            return [app] + al
        else:
            return [al[0]] + add_appointment(al[1:], app)

    ensure(app, is_appointment)
    ensure(cal_day, is_calendar_day)

    return attach_tag('calendar_day', add_appointment(strip_tag(cal_day), app))

#Uppgift 8C
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

def first_appointment(cal_day):
    "calendar_day -> appointment"
    ensure(cal_day, is_calendar_day)
    if is_empty_calendar_day(cal_day):
        raise Exception('Empty calendar day.')
    else:
        return strip_tag(cal_day)[0]

def rest_calendar_day(cal_day):
    "calendar_day -> calendar_day"
    ensure(cal_day, is_calendar_day)
    if is_empty_calendar_day(cal_day):
        return cal_day
    else:
        return attach_tag('calendar_day', strip_tag(cal_day)[1:])


# ----- CALENDAR_MONTH  -----
def new_calendar_month():
    "-> calendar_month"
    return attach_tag('calendar_month', [])

def is_calendar_month(object):
    "Python-object -> Bool"
    return get_tag(object) == 'calendar_month'

def is_empty_calendar_month(cal_mon):
    "calendar_month -> Bool"
    ensure(cal_mon, is_calendar_month)
    return not strip_tag(cal_mon)

def insert_calendar_day(day, cal_day, cal_mon):
    "day x calendar_day x calendar_month -> calendar_month"

    def update(dl):
        if not dl or day_number(day) < day_number(new_day(dl[0][0])):
            return [(strip_tag(day), cal_day)] + dl
        elif day_number(day) == day_number(new_day(dl[0][0])):
            return [(strip_tag(day), cal_day)] + dl[1:]
        else:
            return [dl[0]] + update(dl[1:])

    ensure(day, is_day)
    ensure(cal_day, is_calendar_day)
    ensure(cal_mon, is_calendar_month)

    return attach_tag('calendar_month', update(strip_tag(cal_mon)))

def calendar_day(day, cal_mon):
    "day x calendar_month -> calendar_day"
    ensure(day, is_day)
    ensure(cal_mon, is_calendar_month)
    matched_days = [i for i, x in enumerate(strip_tag(cal_mon))\
                               if x[0] == day_number(day)]
    if not matched_days:
        return new_calendar_day()
    else:
        return strip_tag(cal_mon)[matched_days[0]][1]

def last_booked_day(cal_mon):
    "calendar_month -> Integer"
    ensure(cal_mon, is_calendar_month)
    if is_empty_calendar_month(cal_mon):
        return 0
    else:
        return strip_tag(cal_mon)[-1][0]


# ----- CALENDAR_YEAR -----
def new_calendar_year():
    "-> calendar_year"
    return attach_tag('calendar_year', [])

def is_calendar_year(object):
    "Python-object -> Bool"
    return get_tag(object) == 'calendar_year'

def is_empty_calendar_year(cal_year):
    "calendar_year -> Bool"
    ensure(cal_year, is_calendar_year)
    return not strip_tag(cal_year)

def insert_calendar_month(mon, cal_mon, cal_year):
    "month x calendar_month x calendar_year -> calendar_year"

    def update(ml):
        if not ml or month_number(mon) < month_number(new_month(ml[0][0])):
            return [(strip_tag(mon), cal_mon)] + ml
        elif month_number(mon) == month_number(new_month(ml[0][0])):
            return [(strip_tag(mon), cal_mon)] + ml[1:]
        else:
            return [ml[0]] + update(ml[1:])

    ensure(mon, is_month)
    ensure(cal_mon, is_calendar_month)
    ensure(cal_year, is_calendar_year)

    if is_empty_calendar_month(cal_mon):
        return cal_year
    elif last_booked_day(cal_mon) > number_of_days(mon):
        raise Exception('Too few days in {0}.'.format(month_name(mon)))
    else:
        return attach_tag('calendar_year', update(strip_tag(cal_year)))

def calendar_month(mon, cal_year):
    "month x calendar_year -> calendar_month"

    ensure(mon, is_month)
    ensure(cal_year, is_calendar_year)

    matched_mons = [i for i, x in enumerate(strip_tag(cal_year))\
                               if x[0] == month_name(mon)]
    if not matched_mons:
        return new_calendar_month()
    else:
        return strip_tag(cal_year)[matched_mons[0]][1]


# ----- time_spans, Uppgift 8B -----
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



# =========================================================================
#  A. Calculations
# =========================================================================

#Uppgift 8D
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
            return start, calendar_day

        elif precedes(start, start_time(get_span(first_appointment(calendar_day)))):
            return start, calendar_day
        elif precedes(start, end_time(get_span(first_appointment(calendar_day)))):
            return end_time(get_span(first_appointment(calendar_day))), \
                calendar_day
        return find_first_free_time(rest_calendar_day(calendar_day))

    first_free_time, cal_day = find_first_free_time(cal_day)
    new_ft = find_free_times(first_free_time, cal_day, ft)

    return new_ft


# True iff t1 precedes t2 (before) (else False).
def precedes(t1, t2):
    "time x time -> Bool"
    h1 = get_integer(get_hour(t1))
    m1 = get_integer(get_minute(t1))
    h2 = get_integer(get_hour(t2))
    m2 = get_integer(get_minute(t2))
    return h1 < h2 or (h1 == h2 and m1 < m2)

# True iff t1 and t2 represent the same time.
def is_same_time(t1, t2):
    "time x time -> Bool"
    return get_integer(get_hour(t1)) == get_integer(get_hour(t2)) and\
           get_integer(get_minute(t1)) == get_integer(get_minute(t2))

# Check if t1 precedes t2 or is equal to t2.
def precedes_or_equals(t1, t2):
    "time x time -> Bool"
    return precedes(t1, t2) or is_same_time(t1, t2)

# Return the latter of two time objects.
def latest_time(t1, t2):
    "time x time -> time"
    if precedes(t1, t2):
        return t2
    else:
        return t1

# Return the first of two time objects
def earliest_time(t1, t2):
    "time x time -> time"
    if precedes(t1, t2):
        return t1
    else:
        return t2

# Compares the length of durations. True iff d1 is longer than d2
def is_duration_longer_or_equal(d1, d2):
    "duration x duration -> Bool"
    h1 = get_integer(get_hour(d1))
    m1 = get_integer(get_minute(d1))
    h2 = get_integer(get_hour(d2))
    m2 = get_integer(get_minute(d2))
    
    return h1 > h2 or (h1 == h2 and m1 >= m2)

# Checks if two spans overlap.
def are_overlapping(ts1, ts2):
    "span x span -> Bool"
    return precedes(start_time(ts1), end_time(ts2)) and\
           precedes(start_time(ts2), end_time(ts1))

# Calculates the overlapping part of two time spans.
# This is poorly written, and demands re-implementation (7A).
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

# =========================================================================
#  B. Conversion
# =========================================================================

# Transform a span into a duration. That is, merely calculate the length
# of the span. This should be implemented in 7A.
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

# Create a time object corresponding to the input "HH:MM".
def convert_time(s):
    "String -> time"
    return new_time(new_hour(int(s[0:2])), new_minute(int(s[3:5])))

# Create a duration corresponding to the string "HH:MM". The string must be well-formed
# and the number of hours can consist of an arbitrary number of digits.
def convert_duration(s):
    "String -> duration"
    i = s.find(':')
    return new_duration(new_hour(int(s[0:i])), new_minute(int(s[i+1:])))

# =========================================================================
#  C. Iterator functions
# =========================================================================

# Below are some useful functions for sequentially performing an operation
# on each part of a compound data type (eg printing each day in a 
# calendar_month).

def for_each_month(cal_year, month_fn):
    "calendar_year x (calendar_month ->) ->"
    map(lambda m: month_fn(calendar_month(m, cal_year)), ALL_MONTHS)

def for_each_day(cal_mon, mon, day_fn):
    "calendar_month x (calendar_day ->) ->"
    map(lambda d: day_fn(calendar_day(new_day(d), monalma)),
        list(range(1, number_of_days(mon)+1)))

def for_each_appointment(cal_day, appointment_fn):
    "calendar_day x (appointment ->) ->"
    if not is_empty_calendar_day(cal_day):
        appointment_fn(first_appointment(cal_day))
        for_each_appointment(rest_calendar_day(cal_day), appointment_fn)

        
# Does any appointment during the given calendar day satisfy the 
# predicate?
def some_meeting_satisfies(cal_day, appointment_pred):
    "calendar_day x (appointment -> Bool) -> Bool"
    if is_empty_calendar_day(cal_day):
        return False
    elif appointment_pred(first_appointment(cal_day)):
        return True
    else:
        return some_meeting_satisfies(rest_calendar_day(cal_day),
                                      appointment_pred)


# Keep only time spans that satisfy pred. 
def keep_spans(mts, pred):
    "multiple time spans x (time span -> Bool) -> multiple time spans"
    if is_empty_time_spans(mts):
        return new_time_spans()
    elif pred(first_span(mts)):
        return insert_span(first_span(mts),
                           keep_spans(rest_spans(mts), pred))
    else:
        return keep_spans(rest_spans(mts))       


        
        
        
        
        
        
        
        
        
        
