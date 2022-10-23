import json


class JsonManagement:

    def __init__(self, **kwargs):
        self.base_config = self._load_base_config()
        self.override_config_values = kwargs

    def generate_json(self):
        # return the base configuration if override values
        if not self.override_config_values:
            return self.base_config

        base_file_path = "config/{}/{}.json"

        for key, value in self.override_config_values.items():
            file_path = base_file_path.format(key, value)
            with open(file_path, "r") as f:
                override_config = json.load(f)
                self.base_config.update(override_config)

        return json.dumps(self.base_config, indent=2)

    @staticmethod
    def _load_base_config():
        with open("tenant.json", "r") as f:
            config = json.load(f)
            # TODO make sure the config is valid or other things
            return config


test_config = JsonManagement(program="version3", merchant="version1", env="version2")
print(test_config.generate_json())

