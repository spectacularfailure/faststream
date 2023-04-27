Logger
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

------------------------------------------------------------------------

<a
href="https://github.com/airtai/fastkafka/blob/main/fastkafka/_components/logger.py#L37"
target="_blank" style={{float: 'right', fontSize: 'smaller'}}>source</a>

### get_default_logger_configuration

>      get_default_logger_configuration (level:int=20)

Return the common configurations for the logger

Args: level: Logger level to set

Returns: A dict with default logger configuration

------------------------------------------------------------------------

<a
href="https://github.com/airtai/fastkafka/blob/main/fastkafka/_components/logger.py#L26"
target="_blank" style={{float: 'right', fontSize: 'smaller'}}>source</a>

### supress_timestamps

>      supress_timestamps (flag:bool=True)

Supress logger timestamp

Args: flag: If not set, then the default value **True** will be used to
supress the timestamp from the logger messages

Example on how to useExample on how to use **get_default_logger_configuration** function

``` python
# collapse_output

get_default_logger_configuration()
```

    {'version': 1,
     'disable_existing_loggers': False,
     'formatters': {'standard': {'format': '%(asctime)s.%(msecs)03d [%(levelname)s] %(name)s: %(message)s',
       'datefmt': '%y-%m-%d %H:%M:%S'}},
     'handlers': {'default': {'level': 20,
       'formatter': 'standard',
       'class': 'logging.StreamHandler',
       'stream': 'ext://sys.stdout'}},
     'loggers': {'': {'handlers': ['default'], 'level': 20}}}

------------------------------------------------------------------------

<a
href="https://github.com/airtai/fastkafka/blob/main/fastkafka/_components/logger.py#L80"
target="_blank" style={{float: 'right', fontSize: 'smaller'}}>source</a>

### get_logger

>      get_logger (name:str, level:int=20, add_spaces:bool=True)

Return the logger class with default logging configuration.

Args: name: Pass the **name** variable as name while calling level: Used
to configure logging, default value `logging.INFO` logs info messages
and up. add_spaces:

Returns: The logging.Logger class with default/custom logging
configuration

``` python
logger = get_logger(__name__)
logger.info("hello")
logger = get_logger(__name__)
logger.info("hello")


def f():
    logger.info("hello")


f()
```

    23-04-13 06:25:25.130 [INFO] __main__: hello
    23-04-13 06:25:25.131 [INFO] __main__: hello
    23-04-13 06:25:25.132 [INFO] __main__: hello

Example on how to use **get_logger** function

``` python
# collapse_output

logger = get_logger(__name__)

logger.debug("Debug")
logger.info("info")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")
```

    23-04-13 06:25:25.140 [INFO] __main__: info
    23-04-13 06:25:25.141 [WARNING] __main__: Warning
    23-04-13 06:25:25.142 [ERROR] __main__: Error
    23-04-13 06:25:25.143 [CRITICAL] __main__: Critical

``` python
# collapse_output

supress_timestamps()
logger = get_logger(__name__)

logger.debug("Debug")
logger.info("info")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")
```

    [INFO] __main__: info
    [WARNING] __main__: Warning
    [ERROR] __main__: Error
    [CRITICAL] __main__: Critical

------------------------------------------------------------------------

<a
href="https://github.com/airtai/fastkafka/blob/main/fastkafka/_components/logger.py#L120"
target="_blank" style={{float: 'right', fontSize: 'smaller'}}>source</a>

### set_level

>      set_level (level:int)

Set logger level

Args: level: Logger level to set

``` python
level = logging.ERROR

set_level(level)

# Checking if the logger is set back to logging.WARNING in dev mode
print(logger.getEffectiveLevel())
assert logger.getEffectiveLevel() == level

logger.debug("This is a debug message")
logger.info("This is an info")
logger.warning("This is a warning")
logger.error("This is an error")
```

    40
    [ERROR] __main__: This is an error

``` python
# Reset log level back to info
level = logging.INFO

set_level(level)
logger.info("something")
```

    [INFO] __main__: something

``` python
type(logging.INFO)
```

    int

------------------------------------------------------------------------

<a
href="https://github.com/airtai/fastkafka/blob/main/fastkafka/_components/logger.py#L138"
target="_blank" style={{float: 'right', fontSize: 'smaller'}}>source</a>

### cached_log

>      cached_log (msg:str, level:int, timeout:Union[int,float]=5)

``` python
with unittest.mock.patch("logging.Logger.log") as mock:
    for i in range(3*5-2):
        cached_log(logger, "log me!", level=logging.INFO, timeout=1)
        time.sleep(0.2)
        
    assert mock.call_args_list == [unittest.mock.call(20, 'log me!')]*3
```