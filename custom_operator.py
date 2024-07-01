from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class CustomOperator(BaseOperator):
    @apply_defaults
    def __init__(self, my_param, *args, **kwargs):
        super(CustomOperator, self).__init__(*args, **kwargs)
        self.my_param = my_param

    def execute(self, context):
        # Your custom logic here
        print(f"The value of my_param is: {self.my_param}")