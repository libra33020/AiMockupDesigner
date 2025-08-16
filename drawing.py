import svgwrite
import random

def create_circles_pattern():
    dwg = svgwrite.Drawing(profile='tiny', size=(400, 400))
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))

    for _ in range(50):
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        r = random.randint(5, 30)
        color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
        dwg.add(dwg.circle(center=(x, y), r=r, fill=color))

    return dwg.tostring()

def create_squares_pattern():
    dwg = svgwrite.Drawing(profile='tiny', size=(400, 400))
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))

    for _ in range(50):
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        size = random.randint(10, 50)
        color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
        dwg.add(dwg.rect(insert=(x, y), size=(size, size), fill=color))

    return dwg.tostring()

def create_floral_pattern():
    dwg = svgwrite.Drawing(profile='tiny', size=(400, 400))
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='lightblue')) # Light blue sky

    def draw_flower(group):
        # Petals
        petal_color = f'rgb({random.randint(200, 255)}, {random.randint(100, 200)}, {random.randint(150, 255)})'
        for i in range(6): # 6 petals
            petal = dwg.ellipse(center=(0, -15), r=(5, 15), fill=petal_color)
            petal.rotate(i * 60, center=(0, 0))
            group.add(petal)
        # Center
        center_color = f'rgb({random.randint(200, 255)}, {random.randint(200, 255)}, 0)'
        group.add(dwg.circle(center=(0, 0), r=7, fill=center_color))


    for _ in range(15): # 15 flowers
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        scale = random.uniform(0.5, 1.2)
        flower_group = dwg.g(transform=f"translate({x},{y}) scale({scale})")
        draw_flower(flower_group)
        dwg.add(flower_group)

    return dwg.tostring()

def create_abstract_pattern():
    dwg = svgwrite.Drawing(profile='tiny', size=(400, 400))
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='black')) # Black canvas

    # Add some random lines
    for _ in range(20):
        x1 = random.randint(0, 400)
        y1 = random.randint(0, 400)
        x2 = random.randint(0, 400)
        y2 = random.randint(0, 400)
        color = f'rgb({random.randint(100, 255)}, {random.randint(100, 255)}, {random.randint(100, 255)})'
        stroke_width = random.uniform(0.5, 3)
        dwg.add(dwg.line(start=(x1, y1), end=(x2, y2), stroke=color, stroke_width=stroke_width))

    # Add some random circles
    for _ in range(30):
        x = random.randint(0, 400)
        y = random.randint(0, 400)
        r = random.randint(2, 20)
        color = f'rgb({random.randint(100, 255)}, {random.randint(100, 255)}, {random.randint(100, 255)})'
        dwg.add(dwg.circle(center=(x, y), r=r, fill=color, opacity=random.uniform(0.3, 0.8)))

    return dwg.tostring()

def create_pattern(pattern_type='circles'):
    if pattern_type == 'squares':
        return create_squares_pattern()
    elif pattern_type == 'floral':
        return create_floral_pattern()
    elif pattern_type == 'abstract':
        return create_abstract_pattern()
    else: # Default to circles
        return create_circles_pattern()
