This is an example logging implementation using a setup function and the default `logging.getLogger` function.

Requires the application to independently call the logger setup function once in the application entrypoint,
and then any method can be used in the individual modules to get their appropriate logger,
as these will inhereit the logging basicConfig.