import openai
from flask import *
import config
app = Flask(__name__)
app.secret_key = config.APP_SECRET_KEY
openai.api_key = config.API_KEY

messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        message = "create a concise cover letter with a header to " + request.form["company"] + " for the "+ request.form["position"] + " position. My name is "+ request.form["name"] +". my email is "+ request.form["email"]+ ". my phone number is "+request.form["phone"]+". my address is "+request.form["address"]+". my skills are: "+request.form["skills"]+". Base the cover letter off of this job description: " + request.form["bio"]
        print(message)
        session['message'] = message

        return redirect(url_for('coverLetter'))
    
    return render_template("home.html")

@app.route("/coverLetter", methods=["GET", "POST"])
def coverLetter():
    message = session.get('message')
    # messages.append(
    #     {"role": "user", "content": message},
    # )
    # chat = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo", messages=messages
    # )

    # reply = chat.choices[0].message.content
    test_message = "\n\nNicholas Costa \r\n[ADDRESS] \r\nnicholasmcosta@gmail.com \r\n[PHONE] \r\n\r\n\r\nDear Hiring Manager, \r\n\r\nI am applying for the Software Engineer position at FJA-US Inc. I am confident that my skills, experience, and qualifications align with the requirements described in the job listing. \r\n\r\nMy Bachelor's degree in Computer Science, Software Engineering, and 1-2 years of experience in software development using Java make me a strong candidate for the position. My skills in Python, HTML, JavaScript, Flask, C, and Dialogflow demonstrate my ability to continuously learn and stay up-to-date with emerging technologies and trends. \r\n\r\nAs a team member, I understand and value the importance of writing clean, efficient, and maintainable code that follows coding standards and best practices. I have in-depth knowledge of core Java concepts, algorithms, and object-oriented programming principles. Additionally, I am familiar with Java frameworks such as Spring and Hibernate and have experience developing and designing databases using both SQL and NoSQL databases. \r\n\r\nI have experience collaborating with cross-functional teams to identify requirements and design solutions that ultimately meet business needs. I understand the importance of producing accurate documentation for software systems and applications. \r\n\r\nFinally, I have excellent verbal and written communication skills, and I am comfortable working both independently and as part of a team in a fast-paced environment. I am confident in my problem-solving and analytical abilities and able to apply agile development methodologies to create the best possible outcome. \r\n\r\nThank you for considering my application. I look forward to discussing my candidacy further with FJA-US Inc.\r\n\r\nSincerely, \r\n\r\nNicholas Costa"
    styled_reply = convert_styled_text_to_html(test_message)
    # print(repr(reply))
    # messages.append({"role": "assistant", "content": reply})
    
    return render_template("coverLetter.html", styled_reply=styled_reply)

def convert_styled_text_to_html(styled_text):
    html_text = styled_text.replace('\n\n', '<br><br>').replace('\n', '<br>')
    return html_text

if __name__ == "__main__":
    app.run(debug=True)