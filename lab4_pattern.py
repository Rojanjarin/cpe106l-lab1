class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance


# Test the Singleton pattern
if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()
    
    print(f"logger1 id: {id(logger1)}")
    print(f"logger2 id: {id(logger2)}")
    print(f"Are they the same instance? {logger1 is logger2}")