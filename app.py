from flask import Flask, render_template, Response, request
import drawing

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate')
def generate():
    pattern_type = request.args.get('pattern_type', 'circles')
    svg_data = drawing.create_pattern(pattern_type)
    return Response(svg_data, mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(debug=True)
