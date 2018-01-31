from src.services.log_service import LogService
from src.engine.assemblage import Assemblage
from src.engine.event_manager import EventManager


class AssemblageManager:

    def __init__(self, config):
        self._entity_manager = config['entity_manager']
        self._component_manager = config['component_manager']
        self._templates = config['templates']
        self._assemblages = {}

    def create_assemblage(self, assemblage_type, state):
        """
        Creates a new assemblage of the specified type
        :param assemblage_type: The type of assemblage to be created
        :type assemblage_type: string
        :param state: The state of the assemblage to be created
        :type state: dict

        """
        template = self._get_template(assemblage_type)
        entity = state['entity'] if 'entity' in state else self._entity_manager.create_entity()
        assemblage = template['constructor'](entity)
        components = state['components']
        for component_type in template['components']:
            component = self._component_manager.create_component(entity.id, component_type, components[component_type])
            assemblage.attach_component(component_type, component)
        if assemblage_type not in self._assemblages:
            self._assemblages[assemblage_type] = {}
        self._assemblages[assemblage_type][entity.id] = assemblage

    def destroy_assemblage(self, assemblage_type, entity_id, destroy_entity=False):
        if not self._assemblages[assemblage_type][entity_id]:
            raise Exception('Assemblage type {0} does not exist for entity {1}'.format(assemblage_type, entity_id))
        del self._assemblages[assemblage_type][entity_id]
        if destroy_entity:
            for assemblage_type in self._assemblages:
                if entity_id in self._assemblages[assemblage_type]:
                    del self._assemblages[assemblage_type][entity_id]

    def get_assemblage(self, assemblage_type, entity_id):
        pass

    def _get_template(self, assemblage_type):
        if assemblage_type not in self._templates:
            raise Exception('Template for assemblage type {0} does not exist.'.format(assemblage_type))
        return self._templates[assemblage_type]

    @staticmethod
    def create(config):
        """
        Static factory method
        :param config:
        :type config: dict

        :return: The new AssemblageManager
        :rtype: AssemblageManager
        """
        if 'entity_manager' not in config:
            raise Exception('No entity manager provided for AssemblageManager')
        if 'component_manager' not in config:
            raise Exception('No component manager provided for AssemblageManager')
        if 'templates' not in config:
            raise Exception('No templates provided for AssemblageManager')
        return AssemblageManager(config)
