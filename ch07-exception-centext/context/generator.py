from contextlib import contextmanager


@contextmanager
def my_context_manager():
    print("Entering 'with' context")
    val = object()
    print(id(val))
    try:
        yield val
    except Exception as e:
        print(
            f"{type(e)=} {e=} {e.__traceback__=}"
        )  # type(e)=<class 'Exception'> e=Exception("Exception inside 'with' context") e.__traceback__=<traceback object at 0x000002EE8B87BC40>
    finally:
        print("Exiting 'with' context")


with my_context_manager() as val:
    print("############ Inside 'with' context ############")
    print(id(val))
    raise Exception("Exception inside 'with' context")
    print("This line will never be reached")
print("############ After 'with' context ############")
