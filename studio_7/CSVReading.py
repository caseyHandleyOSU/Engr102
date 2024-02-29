import csv
from Participant import Participant
def main():
    survey_rows = load_csv_file('survey.csv')
    participants = create_participants(survey_rows, input("What currency would you like to filter by? ").upper())
    print("Answer 2:", compare_participants_by(participants, 'industry', 5))
    print("Answer 3:", compare_participants_by(participants, 'age', -1))
    print("Answer 4:", compare_participants_by(participants, 'education', -1))
    print("Answer 5:", compare_participants_by(participants, 'experience', -1))


def create_participants(rows, currency):
    # Generate participant objs from csv file
    participants = []
    for row in rows:
        if(row[7].upper() == currency):
            participants.append(Participant(row[1], row[2], row[5], row[7], row[10], row[13], row[15]))
    print('Answer 1: \n  There are {0} participants who use {1}'.format(len(participants), currency))
    return participants

def compare_participants_by(participants, industry, min_required):
    """
    Abstracted function to compare participants based on an industry, with an optional minimum-required-participants parameter
    """
    sums = get_sum_of_properties(participants, min_required, industry)
    sorted_sums = sorted(sums.items(), key=lambda item: item[1])
    if min_required != 1:
        top_num = sorted_sums[-min_required:]
    else:
        top_num = sorted_sums
    return "{0}".format(format_as_string(dict(reversed(top_num))))

def format_as_string(d):
    """
    Formats a dictionary as a numbered string
    """
    s = ''
    i = 1
    for k in d:
        s += "\n  #{0}: {1}, making ${2:0.2f}/year on average.".format(i, k, d[k])
        i += 1
    return s


def get_sum_of_properties(participants, minimum_in_field, property):
    #keys = get_unique_vals_of_property(participants, compare)
    d = {}
    # Populate dict of industry-[salary] pairs
    for p in participants:
        attr = getattr(p, property)
        try:
            if attr != '':
                l = d[attr]
                l.append(p.salary)
        except KeyError:
            if attr != '':
                d[attr] = [p.salary]
    # Filter out industries with len < 10
    d2 = {}
    for k in d:
        if len(d[k]) >= minimum_in_field:
            d2[k] = avg(d[k])
    return d2    
    
def filter_by_val(participants, property, val):
    filtered = []
    for p in participants:
        if getattr(p, property) == val:
            filtered.append(p)
    return filtered

def avg(list):
    """
    Returns the average value of a given list
    """
    return sum(list) / len(list)

def get_unique_vals_of_property(l, property):
    values = []
    for i in l:
        values.append(getattr(i, property))
    return list(set(values))
    


def load_csv_file(filename):
    rows = []
    with open(filename, 'r', encoding="iso-8859-1") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
        return rows

if __name__ == "__main__":
    main()