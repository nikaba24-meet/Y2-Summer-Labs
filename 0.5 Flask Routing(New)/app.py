from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return ('''<html> 
        <head>
         Hey 
        </head>
         <body>
        <p> Welcome! use this amazing photo gallery: 
        <a href = \'/food1\'>Go to the 1st food photo</a>
        <a href = \'/food3\'>Go to the 3rd food photo</a>
        <a href = \'/pet2\'>Go to the 2nd pet photo</a>
        <a href = \'/space1\'>Go to the 1stspace photo</a>
        </p>
        </body> 
        </html>''')

@app.route('/food1')
def food1():
    return('''<html>
        <p> Heres a muffin :)) 
        <img src = \'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTk1g5ZyrtPuvBypHo6CfnEl00_lWoIF77zUw&s\' 
        alt = \'Muffin\'>
        Go to the next pic <a href = \'/food2\'> prees here </a>
        If you with to return to the home page, press <a href = \'/home\'> here </a>
        </p>
        </html>''')

@app.route('/food2')
def food2():
    return('''<html>
        <p> Here's my favourite food: 
        <img src = \'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJO10Hl3L-GQtHU8b9ZXeMsaFcdXjTwCfaqw&s\'>
        Go to the next pic <a href = \'/food3\'> prees here </a>
        Go to the previous pic <a href = \'/food1\'> prees here </a>

        </p>
        </html>''')

@app.route('/food3')
def food3():
    return('''<html>
        <p> Here's food: 
        <img src = \'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsfR6QS0Jda7nwIK4qy1bSXSRVzJmQxmt0LA&s\'>
        If you with to return to the home page, press <a href = \'/home\'> here </a>
        Go to the previous pic <a href = \'/food2\'> prees here </a>

        </p>
        </html>''')


@app.route('/pet1')
def pet1():
    return('''<html>
        <p> 
        that's my favourite animal :D 
        <img src = \'https://encrypted-tbn0.gstatic.com/images?q=tbn:
        ANd9GcT083jNm5BG2KxvRtpZsY2AfEArtQG26W_gBw&s\' alt = \'hamus pic\'>
        Go to the next pic <a href = \'/pet2\'> prees here </a>
        </p>

        </html>''')


@app.route('/pet2')
def pet2():
    return('''<html>
        <p> 
        that's the kind of dog I have :D 
        <img src = \'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsrd9qldxvbTnD__fMrznM0pBmMY2DI7z3wQ&s\' alt = \'dog pic\'>
        If you with to return to another pet pic, press <a href = \'/pet1\'> here </a>
        Go to the next pic <a href = \'/pet3\'> prees here </a>
        If you wish to return to the home page <a href = \'/home\'> prees here </a>
        </p>

        </html>''')

@app.route('/pet3')
def pet3():
    return('''<html>
        <p> 
        Here's a hamster :D 
        <img src = \'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/PhodopusSungorus_1.jpg/640px-PhodopusSungorus_1.jpg\' 
        alt = \'hamster pic\'>
        Go to the previous pic <a href = \'/pet2\'> prees here </a>
        </p>

        </html>''')


@app.route('/space1')
def space1():
    return('''<html>
        <p> 
        that's a nice pic of the space :D 
        <img src = \'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAHkPFUe7JOZ2rlLsKwcR_DxM25Jkro7tjvQ&s\' alt = \'space1 pic\'>
        If you with to return to the home page, press <a href = \'/home\'> here </a>
        Go to the next pic <a href = \'/space2\'> prees here </a>
        Go to the next next pic <a href = \'/space3\'> prees here </a>
        </p>

        </html>''')

@app.route('/space2')
def space2():
    return('''<html>
        <p> 
        that's a nice pic of the space :D 
        <img src = \'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0vcGORhv8nTrc3C9PN1rgREo-HRy9YKGivw&s\' alt = \'space2 pic\'>
        Go to the next pic <a href = \'/space3\'> prees here </a>
        Go to the previous pic <a href = \'/space1\'> prees here </a>
        </p>

        </html>''')

@app.route('/space3')
def space3():
    return('''<html>
        <p> 
        that's a nice pic of the space :D 
        <img src = \'https://d2pn8kiwq2w21t.cloudfront.net/original_images/1-PIA26274-NuSTAR_Illustration.jpg\' alt = \'space3 pic\' width = 400px>
        Go to the previous pic <a href = \'space2\'> prees here </a>
        Go to the one before the previous pic <a href = \'/space1\'> prees here </a>
        </p>

        </html>''')

    
if __name__ == '__main__':
    app.run(debug=True)