<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            text-align: center;
            padding: 20px;
            font-family: Arial, sans-serif;
        }
        
        .title {
            font-size: 2.5em;
            color: #2c3e50;
            margin-bottom: 30px;
            animation: bounce 2s infinite;
        }
        
        .experiment-area {
            position: relative;
            height: 400px;
            margin: 20px auto;
            width: 300px;
        }
        
        .beaker {
            position: absolute;
            bottom: 50px;
            left: 50%;
            transform: translateX(-50%);
            width: 160px;
            height: 200px;
            background: transparent;
            border: 4px solid #666;
            border-radius: 0 0 20px 20px;
            overflow: hidden;
        }
        
        .liquid {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50%;
            background: rgba(255, 200, 200, 0.8);
            transition: all 0.5s;
        }
        
        .spoon {
            position: absolute;
            top: 50px;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 20px;
            background: #999;
            border-radius: 10px;
            transform-origin: right center;
            transition: transform 1s;
        }
        
        .powder {
            position: absolute;
            top: 0;
            left: 50%;
            width: 40px;
            height: 10px;
            background: #ddd;
            border-radius: 5px;
            transform: translateX(-50%);
        }
        
        .bubbles {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 0;
            transition: height 1s;
            background: repeating-radial-gradient(
                circle,
                rgba(255,255,255,0.8),
                rgba(255,255,255,0.3) 10px,
                rgba(255,255,255,0.8) 20px
            );
            opacity: 0;
        }
        
        .equation {
            margin-top: 20px;
            font-size: 1.2em;
            opacity: 0;
            transition: opacity 1s;
        }
        
        .chemical-text {
            position: absolute;
            font-family: monospace;
            font-size: 1.2em;
        }
        
        .vinegar-text {
            left: 55%;
            bottom: 120px;
        }
        
        .soda-text {
            right: 55%;
            top: 40px;
        }
        
        button {
            padding: 10px 20px;
            font-size: 1.2em;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        button:hover {
            background: #2980b9;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        @keyframes bubble {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">Baking Soda and Vinegar Reaction</h1>
        
        <div class="experiment-area">
            <div class="beaker">
                <div class="liquid"></div>
                <div class="bubbles"></div>
            </div>
            <div class="spoon">
                <div class="powder"></div>
            </div>
            <div class="chemical-text vinegar-text">CH₃COOH</div>
            <div class="chemical-text soda-text">NaHCO₃</div>
        </div>
        
        <button onclick="startExperiment()">Start Experiment</button>
        
        <div class="equation">
            NaHCO₃ (s) + CH₃COOH (aq) → CO₂ (g) + H₂O (l) + NaCH₃COO (aq)
        </div>
    </div>

    <script>
        function startExperiment() {
            const spoon = document.querySelector('.spoon');
            const bubbles = document.querySelector('.bubbles');
            const equation = document.querySelector('.equation');
            const button = document.querySelector('button');
            
            // Disable button during animation
            button.disabled = true;
            
            // Rotate spoon
            spoon.style.transform = 'translateX(-50%) rotate(135deg)';
            
            // After spoon rotation, start reaction
            setTimeout(() => {
                // Hide powder
                document.querySelector('.powder').style.opacity = '0';
                
                // Show bubbles
                bubbles.style.opacity = '1';
                bubbles.style.height = '150%';
                
                // Animate bubbles
                setInterval(() => {
                    bubbles.style.animation = 'bubble 1s infinite';
                }, 100);
                
                // Show equation
                equation.style.opacity = '1';
                
                // Re-enable button after animation
                setTimeout(() => {
                    button.disabled = false;
                }, 2000);
            }, 1000);
        }
    </script>
</body>
</html>
