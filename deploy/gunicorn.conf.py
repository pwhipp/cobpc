import multiprocessing

bind = "0.0.0.0:8200"
workers = multiprocessing.cpu_count() * 2 + 1
