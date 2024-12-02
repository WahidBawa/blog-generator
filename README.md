### Step 1: Install Python
https://www.python.org/downloads/

### Step 2: Install UV:
Open your command line and type in the following once python is installed:
`pip install uv`

### Step 3: Clone this repo and extract it:
This is self explanatory

### Step 4: Install packages
Once you have UV installed, navigate to wherever the code is downloaded to and run the following command:
`uv sync`

### Step 5: Put in your Open AI API key into the .env:
Firstly rename the file called `.example.env` to `.env`. Then inside the file replace the string with your API key.

### Step 6: Create your folder with your blog titles:
Create the folder that will hold your blogs. You can name it whatever feels relevant.
Inside of this folder create a file called `blogs.txt`. Inside of this file put each title of your blog that you want generated on a separate line. There should be no empty lines!

### Step 7: Run the program:
Now finally run `uv run main.py <folder name that you created>`.

So for example, if I created a folder called `test_blogs` then I'd run `uv run main.py test_blogs`.

### Step 8: Profit 😎
