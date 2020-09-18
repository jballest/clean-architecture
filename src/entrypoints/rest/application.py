from src.entrypoints.rest.containers import ApplicationContainer

def create_app():
  container = ApplicationContainer()
  container.config.from_yaml('config.yaml')
  app = container.app()
  app.container = container
  
  app.add_url_rule('/author/create', view_func=container.create_author.as_view(), methods=['POST'])
  return app