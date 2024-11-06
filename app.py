import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@shadcn/ui';
import { motion } from 'framer-motion';

const BakingSodaVinegarReaction = () => {
  const [showReaction, setShowReaction] = useState(false);

  const handleStartExperiment = () => {
    animateSpoon();
    setTimeout(() => {
      setShowReaction(true);
    }, 1000);
  };

  const animateSpoon = () => {
    const spoon = document.querySelector('.spoon');
    spoon.classList.add('pouring');

    // Add light grey powder as a ball on the spoon
    const powder = document.createElement('div');
    powder.classList.add('powder');
    spoon.appendChild(powder);

    // Make the powder fall into the beaker when the spoon bends
    setTimeout(() => {
      powder.classList.add('fall');
    }, 500);
  };

  return (
    <Card className="w-full max-w-4xl">
      <CardHeader>
        <CardTitle>Baking Soda and Vinegar Reaction Simulation</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="experiment-container">
          <div className="beaker">
            <div className="label">CH₃COOH</div>
            {showReaction && (
              <motion.div
                className="reaction"
                initial={{ height: 0 }}
                animate={{ height: '300px', opacity: 0 }}
                transition={{ duration: 2, ease: 'easeOut' }}
              />
            )}
          </div>
          <div className="spoon">
            <div className="spoon-content">NaHCO₃</div>
            <div className="powder"></div>
          </div>
        </div>
        <button
          onClick={handleStartExperiment}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
        >
          Start Experiment
        </button>
        <p className="mt-4">
          <strong>Chemical Equation:</strong> NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO
        </p>
      </CardContent>
    </Card>
  );
};

export default BakingSodaVinegarReaction;
