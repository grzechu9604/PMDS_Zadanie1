import random


AMOUNT_OF_HOTELS = 100
AMOUNT_OF_PEOPLE = 1000
AMOUNT_OF_DAYS = 1000
PROBABILITY_OF_BEING_IN_HOTEL = 0.1


def check_if_met_more_than_once(first_list, secound_list, suspects_pairs_count, suspicious_meeting_count):
    meeting_counter = 0

    for i in first_list:
        for j in secound_list:
            if i == j :
                meeting_counter += 1

    if meeting_counter > 1:
        suspects_pairs_count += 1

    return suspects_pairs_count, suspicious_meeting_count


def is_in_hotel():
    return random.random() <= PROBABILITY_OF_BEING_IN_HOTEL


def calculate_hotel():
    return random.randint(1, AMOUNT_OF_HOTELS)


def main():

    list_of_hotels_visits = []
    for i in range(AMOUNT_OF_PEOPLE):
        list_of_hotels_visits.append([])

    for day in range(AMOUNT_OF_DAYS):
        for person in range(AMOUNT_OF_PEOPLE):
            if is_in_hotel():
                hotel = calculate_hotel()
                list_of_hotels_visits[person].append((day, hotel))

    suspect_pairs_count = 0
    suspect_meetings = 0

    for person in range(AMOUNT_OF_PEOPLE):
        for person_to_check in range(person + 1, AMOUNT_OF_PEOPLE):
            suspect_pairs_count, suspect_meetings = check_if_met_more_than_once(list_of_hotels_visits[person],
                                        list_of_hotels_visits[person_to_check],
                                        suspect_pairs_count,
                                        suspect_meetings)

    print('x')


main()
