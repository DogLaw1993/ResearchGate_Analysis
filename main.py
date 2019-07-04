try:
    import Queue as queue
except:
    import queue
from crawler import co_author_crawlers

init = {'*****': '***********************************'}
nodes = []
edges = []


def main():
    q = queue.Queue()
    q.put(init)
    count = 0
    # k = int(input("请输入一个数"))
    k = 2

    while count < k:
        if q.empty():
            print("结束")

        sizeQueue = q.qsize()
        i = 0
        while i < sizeQueue:
            name_url_pair = q.get()
            temp = co_author_crawlers.process(co_author_crawlers(), name_url_pair, nodes, edges)
            for key, value in temp.items():
                q.put({key: value})
            i += 1
        count = count + 1

    print(nodes)
    print(edges)


if __name__ == '__main__':
    main()
