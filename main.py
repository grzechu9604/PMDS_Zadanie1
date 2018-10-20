import numpy as np


AMOUNT_OF_HOTELS = 10**2                # parameter Nh
AMOUNT_OF_PEOPLE = 10**4                # parameter N
AMOUNT_OF_DAYS = 10**2                  # parameter Nd
PROBABILITY_OF_BEING_IN_HOTEL = 0.1     # parameter P


def main():
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

    for person in range(AMOUNT_OF_PEOPLE):
        for second_person in range(person + 1, AMOUNT_OF_PEOPLE):
            if meeting_counter[person][second_person] > 1:
                suspicious_pairs += 1
                suspicious_days_pairs += int((meeting_counter[person][second_person]
                                          * (meeting_counter[person][second_person] - 1)) / 2)
            if meeting_counter[person][second_person] > 0:
                if meeting_counter[person][second_person] in histogram:
                    histogram[meeting_counter[person][second_person]] += 1
                else:
                    histogram[meeting_counter[person][second_person]] = 1

    print("Podejrzane pary \"osób i dni\": ",  suspicious_days_pairs)
    print("Podejrzane pary: ", suspicious_pairs)
    print("Histogram: ", histogram)


main()
