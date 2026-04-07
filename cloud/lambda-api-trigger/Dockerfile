FROM public.ecr.aws/lambda/python:3.12

WORKDIR /var/task

COPY . .

RUN pip install --no-cache-dir -e .

CMD ["handler.handler"]
