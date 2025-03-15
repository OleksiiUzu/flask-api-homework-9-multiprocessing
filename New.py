import random
import time
import multiprocessing
import concurrent.futures


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


def happy_ticket_check(ticket_number: str) -> bool:
    number = [int(i) for i in ticket_number]
    first_part = number[:len(number) // 2]
    second_part = number[len(number) // 2:]
    return sum(first_part) == sum(second_part)


def happy_tickets_count(ticket_number_range: int):
    ticket_count = 0
    for _ in range(0, ticket_number_range + 1):
        number = str(_).zfill(len(str(ticket_number_range)))
        if (len(number) % 2) == 0 and happy_ticket_check(number):
            ticket_count += 1
    return ticket_count


@timer(message='threads')
def use_threads():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        result = sum(executor.map(happy_tickets_count, [999_999] * 4))
    return result


@timer(message='processes')
def use_process():
    with multiprocessing.Pool(4) as pool:
        result = sum(pool.map(happy_tickets_count, [999_999] * 4))
    return result


if __name__ == "__main__":
    use_threads()
    use_process()
