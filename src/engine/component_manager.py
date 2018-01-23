class ComponentManager:

    def __init__(self):
        self._templates = {}
        self._components = {}

    def create_component(self, entity_id, component_type, state):
        if self.has_component(entity_id, component_type):
            raise Exception('Component type ' + component_type + ' for entity id ' + entity_id + ' already exists')
        template = self._get_template(component_type)
        component = template(entity_id, state)
        if component_type not in self._components:
            self._components[component_type] = {}
        self._components[component_type][entity_id] = component

    def destroy_component(self, entity_id, component_type):
        if not self.has_component(entity_id, component_type):
            raise Exception('Component type ' + component_type + ' for entity id ' + entity_id + ' does not exist')
        components = self._components[component_type]
        del components[entity_id]

    def update_component(self, entity_id, component_type, state):
        component = self.get_component(entity_id, component_type)
        component.update(state)

    def get_component(self, entity_id, component_type):
        if not self.has_component(entity_id, component_type):
            raise Exception('Component type ' + component_type + ' for entity id ' + entity_id + ' does not exist')
        components = self._components[component_type]
        return components[entity_id]

    def has_component(self, entity_id, component_type):
        components = self._components[component_type]
        return entity_id in components

    def _has_template(self, component_type):
        return component_type in self._templates

    def _add_template(self, component_type, template):
        if self._has_template(component_type):
            raise Exception('Template for ' + component_type + ' already exists')
        self._templates[component_type] = template

    def _get_template(self, component_type):
        if not self._has_template(component_type):
            raise Exception('Template for ' + component_type + ' does not exist')
        return self._templates[component_type]

    @staticmethod
    def create():
        pass
