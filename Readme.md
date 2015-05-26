## WSGI Hello World App

I'm only able to get this app reporting data when manually integrating and wrapping the application.
The command I'm using is:

```
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program uwsgi --http :8000 --wsgi-file app.py --single-interpreter --enable-threads
```

When I try to start the app using the wrapper script I don't see any data.  There's not Harvest thread or Activate thread.  The logs stop here:

```
2015-05-26 14:50:09,054 (43202/MainThread) newrelic.config DEBUG - register module ('gevent.monkey', 'newrelic.hooks.coroutines_gevent', 'instrument_gevent_monkey')
2015-05-26 14:50:09,054 (43202/MainThread) newrelic.config DEBUG - register module ('weberror.errormiddleware', 'newrelic.hooks.middleware_weberror', 'instrument_weberror_errormiddleware')
2015-05-26 14:50:09,054 (43202/MainThread) newrelic.config DEBUG - register module ('weberror.reporter', 'newrelic.hooks.middleware_weberror', 'instrument_weberror_reporter')
2015-05-26 14:50:09,054 (43202/MainThread) newrelic.config DEBUG - register module ('thrift.transport.TSocket', 'newrelic.hooks.external_thrift', 'instrument')
2015-05-26 14:50:09,054 (43202/MainThread) newrelic.config DEBUG - register module ('gearman.client', 'newrelic.hooks.application_gearman', 'instrument_gearman_client')
2015-05-26 14:50:09,054 (43202/MainThread) newrelic.config DEBUG - register module ('gearman.connection_manager', 'newrelic.hooks.application_gearman', 'instrument_gearman_connection_manager')
2015-05-26 14:50:09,054 (43202/MainThread) newrelic.config DEBUG - register module ('gearman.worker', 'newrelic.hooks.application_gearman', 'instrument_gearman_worker')
```

Manually integrating and wrapping the application object with `@newrelic.agent.wsgi_application()` sends data to the UI.
