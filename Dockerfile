# Container image that runs your code
FROM ruby:2.7

COPY Gemfile /Gemfile
COPY Gemfile.lock /Gemfile.lock
RUN bundle install --gemfile=/Gemfile

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
