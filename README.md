# python-conf-manage
json configuration management in python projects 

you can override the below config by passing your own version of `program`, `merchant` and `env`

`test_config = JsonManagement(program="version3", merchant="version2", env="version3")`

    {
        "name": "Royal Bank of Canada",
        "program": {
            "name": "test-a"
        },
        "merchant": {
            "name": "microsoft",
            "payment-product": {
                "name": "zero-percent-loan"
            }
        },
        "env": {
            "name": "qa",
            "api": "https://gorest.co.in/public/v2/users",
            "timeout": 60000,
            "cypress": {
                "response-timeout": 240000,
                "video-compression": false
            }
        }
    }
