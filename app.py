import React, { useState } from 'react';
import styled, { keyframes } from 'styled-components';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 2rem;
`;

const ExperimentContainer = styled.div`
  position: relative;
  width: 100%;
  max-width: 600px;
  height: 400px;
  margin-bottom: 2rem;
`;

const Burette = styled.div`
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 20px;
  height: 200px;
  background-color: #ddd;
  border: 2px solid #aaa;
`;

const BuretteTab = styled.div`
  position: absolute;
  bottom: -12px;
  left: 50%;
  transform: translateX(-50%);
  width: 30px;
  height: 12px;
  background-color: #aaa;
  border-radius: 2px;
`;

const Beaker = styled.div`
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 120px;
  height: 180px;
  border: 3px solid #ddd;
  border-radius: 5px;
  overflow: hidden;
  background-color: #ff6666;
  transition: background-color 1s ease;
`;

const dropAnimation = keyframes`
  0% { top: 10px; opacity: 1; }
  90% { top: 150px; opacity: 1; }
  100% { top: 180px; opacity: 0; }
`;

const Drop = styled.div`
  position: absolute;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  width: 8px;
  height: 12px;
  background-color: blue;
  border-radius: 50%;
  opacity: 0;
  animation: ${dropAnimation} 2s forwards;
  animation-delay: ${(props) => props.delay}s;
`;

const AcidBaseChart = () => {
  const [showExperiment, setShowExperiment] = useState(false);

  const handleStartExperiment = () => {
    setShowExperiment(true);
  };

  // Generate sample pH data
  const pHData = Array.from({ length: 100 }, (_, i) => {
    const volume = (i / 99) * 25;
    return {
      volume: volume.toFixed(2),
      pH: 0 + (7 - 0) * (1 - Math.exp(-0.3 * (volume - 12.5))) + (14 - 7) * (1 - Math.exp(-0.3 * (volume - 12.5))),
    };
  });

  return (
    <Container>
      <h1 className="title">Acid-Base Titration</h1>
      <ExperimentContainer>
        {showExperiment && (
          <>
            <Burette>
              <BuretteTab />
              <Drop delay={0} />
              <Drop delay={0.5} />
              <Drop delay={1} />
            </Burette>
            <Beaker className="color-change" />
          </>
        )}
      </ExperimentContainer>
      <button onClick={handleStartExperiment}>Start Experiment</button>
      <LineChart width={600} height={400} data={pHData}>
        <XAxis dataKey="volume" type="number" domain={[0, 25]} />
        <YAxis type="number" domain={[0, 14]} />
        <CartesianGrid strokeDasharray="3 3" />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="pH" stroke="#8884d8" />
      </LineChart>
    </Container>
  );
};

export default AcidBaseChart;
