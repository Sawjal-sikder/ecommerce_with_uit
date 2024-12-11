
## Setup Instructions

### Prerequisites

- Python 3.x
- Django 5.1.4
- Virtualenv

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd ecommerce_with_uit
    ```

2. Create a virtual environment:
    ```sh
    python -m venv env
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source env/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

5. Apply migrations:
    ```sh
    python manage.py migrate
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/` to see the application.

## Running Tests

To run the tests, use the following command:
```sh
python manage.py test