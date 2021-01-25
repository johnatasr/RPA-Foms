import multiprocessing as mp
import numpy as np
import time


def my_function(i, param1, param2, param3):
    result = param1 ** 2 * param2 + param3
    time.sleep(2)
    return (i, result)


def get_result(result):
    global results
    results.append(result)


if __name__ == '__main__':
    # params = np.random.random((10, 3)) * 100.0
    # results = []
    # ts = time.time()
    # for i in range(0, params.shape[0]):
    #     get_result(my_function(i, params[i, 0], params[i, 1], params[i, 2]))
    # print('Time in serial:', time.time() - ts)
    # print(results)
    #
    # results = []
    # ts = time.time()
    # pool = mp.Pool(mp.cpu_count())
    # for i in range(0, params.shape[0]):
    #     pool.apply_async(my_function, args=(i, params[i, 0], params[i, 1], params[i, 2]), callback=get_result)
    # pool.close()
    # pool.join()
    # print('Time in parallel:', time.time() - ts)
    # print(results)

    print(mp.cpu_count())


# from multiprocessing.dummy import Pool
# import datetime
#
#
# def rpa(nome):
#     # print(f"{params} - {date}")
#     a = nome
#     return a
#
#
# # def worker(params):
# #     data_atual = datetime.now()
# #
# #     try:
# #         rpa(params, data_atual)
# #     except Exception as exception:
# #         print(exception)
#
# def callback(nome):
#     print(nome)
#
# def main_thread(nome):
#     pool_threads= 8
#     div = 10
#     try:
#         with Pool(pool_threads) as pool:
#             # for i in range(1 , div):
#             re = pool.apply_async(rpa, args=[nome])
#             re.get()
#
#         pool.close()
#         pool.join()
#
#     except Exception as error:
#         print(error)
#
# if __name__ == "__main__":
#     params = "Johnatas"
#     aa =1
#     main_thread(params)


#
# import time
# from multiprocessing.pool import ThreadPool as Pool
# import rpa as r
#
# def async_function(name):
#     r.init()
#     r.url('https://www.google.com')
#     r.type('//*[@name="q"]', 'decentralization[enter]')
#     print(r.read('result-stats'))
#     r.snap('page', 'results.png')
#     r.close()
#     return name
#
#
# def callback_function(name):
#     print("Executing")
#
#
# def main():
#     name = "John"
#     pool = Pool(processes=10)
#     new_callback_function = \
#         lambda new_name: callback_function(name)
#
#     pool.apply_async(
#         async_function,
#         args=[name],
#         callback=new_callback_function
#     )
#
#     # from functools import partial
#     #
#     # for age, name in enumerate(['jack', 'jill', 'james']):
#     #
#     #     new_callback_function = partial(callback_function, age=age)
#     #     pool.apply_async(
#     #         async_function,
#     #         args=[name],
#     #         callback=new_callback_function
#     #     )
#
#     pool.close()
#     pool.join()
#
# main()
#
#
