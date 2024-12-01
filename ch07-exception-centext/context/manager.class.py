class MyContextManager:
    def __init__(self):
        print("MyContextManager init", id(self))  # MyContextManager init 2686836426464

    def __enter__(self):
        print("Entering 'with' context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(
            f"{exc_type=} {exc_val=} {exc_tb=}"
        )  # exc_type=<class 'Exception'> exc_val=Exception("Exception inside 'with' context") exc_tb=<traceback object at 0x0000027193EE1D40>

        print("Exiting 'with' context")
        return True


with MyContextManager() as mgr:
    print("############ Inside 'with' context ############")
    print(id(mgr))  # 2686836426464
    raise Exception("Exception inside 'with' context")
    print("This line will never be reached")

print("############ After 'with' context ############")
