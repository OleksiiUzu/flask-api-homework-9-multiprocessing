import random
import time
import multiprocessing
import concurrent.futures


# Чисто для виведення інформації
def timer(message=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            random.seed()
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print('Total Happy Tickets: ', result)
            print(f'Time taken in seconds with {message}: ', end - start)
        return wrapper
    return decorator


class HappyTickets:
    def __init__(self, threads_or_processes_number: int, ticket_number_range: int, number_of_tickets: int):
        self.happy_ticket = 0
        self.threads_or_processes_number = threads_or_processes_number
        self.ticket_number_length = ticket_number_range
        self.number_of_tickets = number_of_tickets

    def happy_ticket_check(self, ticket_number: int) -> bool:
        # Функція перевіряє значення(щасливий білет чи ні)
        random_number_str = str(ticket_number).zfill(10)
        random_number_str = [int(i) for i in random_number_str]
        first_part = random_number_str[:len(random_number_str) // 2]
        second_part = random_number_str[len(random_number_str) // 2:]
        if sum(first_part) == sum(second_part):
            self.happy_ticket = sum(first_part) == sum(second_part)
            return self.happy_ticket  # Повертає True якщо білетик щасливий

    def happy_tickets_count(self, number_iterations: int) -> int:
        ticket_count = 0
        for _ in range(number_iterations):
            random_number = random.randint(0, self.ticket_number_length)
            if (random_number % 2) == 0:
                self.happy_ticket = self.happy_ticket_check(random_number)
            if self.happy_ticket:
                ticket_count += 1
        return ticket_count  # Повертає кількість щасливих білетів

    @timer(message='threads')
    def use_threads(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads_or_processes_number) as executor:
            result = sum(executor.map(self.happy_tickets_count,
                                      [self.number_of_tickets] * self.threads_or_processes_number))
        return result

    @timer(message='processes')
    def use_process(self):
        with multiprocessing.Pool(self.threads_or_processes_number) as pool:
            result = sum(pool.map(self.happy_tickets_count,
                                  [self.number_of_tickets] * self.threads_or_processes_number))
        return result


if __name__ == "__main__":
    happy = HappyTickets(4, 999_999_999_9, 100000)
    happy.use_threads()
    happy.use_process()
