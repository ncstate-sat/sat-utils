This example uses a singleton mixin for the `SATLogger` class, so no setup function call is necessary.

The first time the `SATLogger` is used to initiate a logger, the setup function is called by the Singleton mixin.
The benefit here is that the application entrypoint doesn't have to call a setup function;
every file in the application will just have `logger = SATLogger(__name__)` at the top,
which is how they currently work.

The downsides to this approach are
- a bit of increased complexity
- less flexibiliy or visibility into how the basicConfig is being set.
- Not really a way to parameterize the setup function; have to rely on one that pulls from environment variables
    implicitly instead of passing values in as arguments.
    We could add parameterization to the class init, but that would not function in an obivous way,
    since it would only pull those parameters in the first time the class was called,
    and just ignore them every other time.
