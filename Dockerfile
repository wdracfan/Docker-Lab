FROM jupyterhub/jupyterhub-demo

COPY jupyterhub_config.py .

EXPOSE 80

CMD ["jupyterhub"]