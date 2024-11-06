import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';

const ChemicalReactionDemo = () => {
  const [isAnimating, setIsAnimating] = useState(false);
  const [step, setStep] = useState(0);

  const startAnimation = () => {
    setIsAnimating(true);
    setStep(1);
    // Sequence the animation steps
    setTimeout(() => setStep(2), 1000); // Spoon tilt
    setTimeout(() => setStep(3), 2000); // Powder fall
    setTimeout(() => setStep(4), 2500); // Reaction
    setTimeout(() => {
      setStep(5);
      setIsAnimating(false);
    }, 5000); // Show equation
  };

  return (
    <div className="w-full max-w-2xl mx-auto p-4">
      <Card className="bg-white">
        <CardContent className="p-6">
          <h1 className="text-2xl font-bold text-center mb-8">
            Baking Soda and Vinegar Reaction
          </h1>
          
          <div className="relative w-full h-96">
            {/* SVG Container */}
            <svg viewBox="0 0 400 400" className="w-full h-full">
              {/* Beaker */}
              <path
                d="M100 150 L100 350 L300 350 L300 150 L280 150 L280 180 L120 180 L120 150 Z"
                fill="none"
                stroke="black"
                strokeWidth="2"
              />
              
              {/* Vinegar solution */}
              <path
                d="M120 180 L120 350 L280 350 L280 180 Z"
                fill="#ffcdd2"
                opacity="0.7"
              />
              
              {/* Spoon */}
              <g transform={`rotate(${step >= 2 ? '45' : '0'} 250 100)`}>
                <path
                  d="M200 100 L300 100 L310 90 L300 80 L200 80 Z"
                  fill="#d3d3d3"
                  stroke="black"
                />
                <circle cx="200" cy="90" r="15" fill="#d3d3d3" stroke="black" />
                
                {/* Baking soda in spoon (visible only before pouring) */}
                {step < 2 && (
                  <circle cx="250" cy="90" r="10" fill="white" stroke="#d3d3d3" />
                )}
              </g>
              
              {/* Label for NaHCO₃ */}
              <text x="320" y="95" className="text-sm">NaHCO₃</text>
              
              {/* Label for CH₃COOH */}
              <text x="320" y="250" className="text-sm">CH₃COOH</text>
              
              {/* Falling powder animation */}
              {step === 2 && (
                <path
                  d="M250 120 Q250 200 250 280"
                  stroke="white"
                  strokeWidth="4"
                  strokeDasharray="4,4"
                >
                  <animate
                    attributeName="stroke-dashoffset"
                    from="0"
                    to="32"
                    dur="1s"
                    repeatCount="indefinite"
                  />
                </path>
              )}
              
              {/* Reaction bubbles */}
              {step >= 3 && (
                <g>
                  {[...Array(20)].map((_, i) => (
                    <circle
                      key={i}
                      cx={200 + Math.random() * 80 - 40}
                      cy={350 - Math.random() * 200}
                      r={5 + Math.random() * 10}
                      fill="white"
                      opacity="0.6"
                    >
                      <animate
                        attributeName="cy"
                        from="350"
                        to="100"
                        dur={`${1 + Math.random()}s`}
                        repeatCount="indefinite"
                      />
                      <animate
                        attributeName="opacity"
                        from="0.6"
                        to="0"
                        dur={`${1 + Math.random()}s`}
                        repeatCount="indefinite"
                      />
                    </circle>
                  ))}
                </g>
              )}
            </svg>
          </div>
          
          {/* Chemical equation */}
          {step === 5 && (
            <div className="text-center mt-4 p-4 bg-gray-50 rounded">
              <p className="font-mono">
                NaHCO₃ (s) + CH₃COOH (aq) → CO₂ (g) + H₂O (l) + NaCH₃COO (aq)
              </p>
            </div>
          )}
          
          <div className="text-center mt-4">
            <Button
              onClick={startAnimation}
              disabled={isAnimating}
              className="bg-blue-500 hover:bg-blue-600 text-white"
            >
              {isAnimating ? "Reaction in Progress..." : "Start Experiment"}
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default ChemicalReactionDemo;
