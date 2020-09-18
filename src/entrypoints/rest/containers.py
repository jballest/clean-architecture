from dependency_injector import containers, providers
from dependency_injector.ext import flask
from flask import Flask
from src.core.uses_cases.admin_coordinator import AdminCoordinator
from src.dataproviders.json.author_repository import JsonAuthorRepository
from src.dataproviders.json.book_repository import JsonBookRepository
from src.entrypoints.rest import author_controller

class ApplicationContainer(containers.DeclarativeContainer):
  app = flask.Application(Flask, __name__)
  config = providers.Configuration()
  
  json_book_repository = providers.Factory(
    JsonBookRepository,
    filename=config.author_controller.filename
  )

  json_author_repository = providers.Factory(
    JsonAuthorRepository,
    filename=config.author_controller.filename
  )

  json_admin_coordinator = providers.Factory(
    AdminCoordinator,
    book_repository=json_book_repository,
    author_repository=json_author_repository
  )

  create_author = flask.View(
    author_controller.store,
    admin_coordinator=json_admin_coordinator
  )
