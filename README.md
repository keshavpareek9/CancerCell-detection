Leukemia Detection with Image Processing
This Python script utilizes OpenCV to detect and analyze leukemia cells in medical images. It applies various image processing techniques to identify and categorize the cells based on their characteristics.

Features
Image Processing: Utilizes OpenCV to preprocess and analyze medical images.
Contour Detection: Identifies contours in the image to locate potential leukemia cells.
Classification: Classifies the detected cells based on their size, providing insights into the stage of leukemia.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/<username>/<repository>.git
Install Dependencies:

Ensure you have Python installed on your system along with the necessary packages listed in the requirements.txt file. You can install them using pip:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Script:

Execute the main.py script with the path to the medical image as a parameter:

bash
Copy code
python main.py /path/to/medical/image.jpg
View Results:

The script will display the original image along with the detected contours. It will also print diagnostic information based on the detected cells, such as the number of circles, average radius, and the stage of leukemia.

Notes
Ensure the medical image is in a supported format (e.g., JPEG, PNG).
Adjust the threshold and blur parameters in the script as needed for optimal contour detection.
This script is for educational and demonstrative purposes and should not be used as a substitute for professional medical diagnosis.
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
