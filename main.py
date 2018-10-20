import numpy as np


AMOUNT_OF_HOTELS = 10**2                # parameter Nh
AMOUNT_OF_PEOPLE = 10**4                # parameter N
AMOUNT_OF_DAYS = 10**2                  # parameter Nd
PROBABILITY_OF_BEING_IN_HOTEL = 0.1     # parameter P

AMOUNT_OF_REPETITIONS = 5


def update_global_histogram(global_histogram: dict, local_histogram: dict):
    for key, value in local_histogram.items():
        if key in global_histogram:
            global_histogram[key] += value
        else:
            global_histogram[key] = value


def average_histogram(histogram: dict):
    for key, value in histogram.items():
        histogram[key] = value // AMOUNT_OF_REPETITIONS


def main():
    global_suspicious_pairs = 0
    global_suspicious_days_pairs = 0
    global_histogram = dict()
    global_suspicious_people_amount = 0

    for k in range(AMOUNT_OF_REPETITIONS):
        print("Powtórzenie nr: ", k + 1)
        suspicious_pairs = 0
        suspicious_days_pairs = 0
        histogram = dict()

        meeting_counter = np.zeros((AMOUNT_OF_PEOPLE, AMOUNT_OF_PEOPLE))
        hotels_guests = [[] for i in range(AMOUNT_OF_HOTELS)]

        for day in range(AMOUNT_OF_DAYS):
            random_vector = np.random.rand(AMOUNT_OF_PEOPLE)
            [[hotels_guests[np.random.randint(AMOUNT_OF_HOTELS)].append(person)
              if random_vector[person] <= PROBABILITY_OF_BEING_IN_HOTEL else None] for person in range(AMOUNT_OF_PEOPLE)]

            for hotel in hotels_guests:
                for guest in range(hotel.__len__()):
                    for second_gest in range(guest + 1, hotel.__len__()):
                        meeting_counter[hotel[guest]][hotel[second_gest]] += 1
                hotel.clear()

        suspicious_people = np.zeros(AMOUNT_OF_PEOPLE)

        for person in range(AMOUNT_OF_PEOPLE):
            for second_person in range(person + 1, AMOUNT_OF_PEOPLE):
                if meeting_counter[person][second_person] > 1:
                    suspicious_pairs += 1
                    suspicious_days_pairs += (meeting_counter[person][second_person]
                                                  * (meeting_counter[person][second_person] - 1)) // 2
                    suspicious_people[person] = 1
                    suspicious_people[second_person] = 1
                if meeting_counter[person][second_person] > 0:
                    if meeting_counter[person][second_person] in histogram:
                        histogram[meeting_counter[person][second_person]] += 1
                    else:
                        histogram[meeting_counter[person][second_person]] = 1
        suspicious_people_amount = np.sum(suspicious_people)

        print("Podejrzane pary \"osób i dni\": ",  suspicious_days_pairs)
        print("Podejrzane pary: ", suspicious_pairs)
        print("Histogram: ", histogram)
        print("Liczba podejrzanych osób: ", suspicious_people_amount)

        global_suspicious_pairs += suspicious_pairs
        global_suspicious_days_pairs += suspicious_days_pairs
        global_suspicious_people_amount += suspicious_people_amount
        update_global_histogram(global_histogram, histogram)

    average_histogram(global_histogram)
    print("Wyniki uśrednione:")
    print("Uśrednione podejrzane pary \"osób i dni\": ", global_suspicious_pairs // AMOUNT_OF_REPETITIONS)
    print("Uśrednione podejrzane pary: ", global_suspicious_days_pairs // AMOUNT_OF_REPETITIONS)
    print("Uśredniony histogram: ", global_histogram)
    print("Uśredniona liczba podejrzanych osób: ", global_suspicious_people_amount // AMOUNT_OF_REPETITIONS)


main()
