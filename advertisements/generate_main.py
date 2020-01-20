from jinja2 import Environment, FileSystemLoader
import os
 
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
print(templates_dir)
env = Environment( loader = FileSystemLoader(templates_dir) )
print(env.list_templates())
template = env.get_template('temlate.html')

os.walk(os.path.abspath(__file__))

directories = [x[0] for x in os.walk(os.getcwd())]

end_d = []

for d in directories:
    tmp = d.split("\\")
    print(tmp[-1])
    if tmp[-1] not in ["html", "templates", "advertisements", "index_img"]:
    # or "template" or "advertisements":
        print("asdasd")
        end_d.append(tmp[-1])

enndd_d = []
for d in end_d: 
    tmp = d.split("_")
    enndd_d.append(" ".join(tmp))

print(end_d)

filename = os.path.join(root, 'html', 'template.html')

print(filename)
print("hahahah")

with open(filename, 'wb') as fh:
    fh.write(template.render(
        
        advertisements    = enndd_d,
    ).encode('utf-8'))