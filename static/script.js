document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-btn');
    const svgContainer = document.getElementById('svg-container');
    const patternTypeSelect = document.getElementById('pattern-type');

    const fetchAndDisplaySVG = () => {
        const patternType = patternTypeSelect.value;
        fetch(`/api/generate?pattern_type=${patternType}`)
            .then(response => response.text())
            .then(svgData => {
                svgContainer.innerHTML = svgData;
            })
            .catch(error => {
                console.error('Error fetching SVG:', error);
            });
    };

    generateBtn.addEventListener('click', fetchAndDisplaySVG);

    const downloadBtn = document.getElementById('download-btn');
    downloadBtn.addEventListener('click', () => {
        const svgData = svgContainer.innerHTML;
        if (svgData) {
            const blob = new Blob([svgData], { type: 'image/svg+xml' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'design.svg';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        } else {
            alert('No design to download. Please generate one first.');
        }
    });

    // Load an initial pattern
    fetchAndDisplaySVG();
});
