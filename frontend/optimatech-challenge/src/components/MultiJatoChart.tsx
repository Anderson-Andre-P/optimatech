import React from 'react';
import Plot from 'react-plotly.js';

interface ChartProps {
  tempo: string[];
  temperaturaEntrada: number[];
  temperaturaSaida: number[];
  aberturaValvulaAlimentacao: number[];
  nivelCozedor: number[];
  capacitanciaCozedor: number[];
  pressaoCozedor: number[];
  titleOfChart: string;
}

function MultijatoChart({
  tempo,
  temperaturaEntrada,
  temperaturaSaida,
  aberturaValvulaAlimentacao,
  nivelCozedor,
  capacitanciaCozedor,
  pressaoCozedor,
  titleOfChart,
}: ChartProps) {
  return (
    <Plot
      data={[
        {
          x: tempo,
          y: temperaturaEntrada,
          type: 'scatter',
          mode: 'lines+markers',
          name: 'Temp. Entrada',
          marker: { color: 'red' },
        },
        {
          x: tempo,
          y: temperaturaSaida,
          type: 'scatter',
          mode: 'lines+markers',
          name: 'Temp. Saída',
          marker: { color: 'blue' },
        },
        {
          x: tempo,
          y: nivelCozedor,
          type: 'scatter',
          mode: 'lines+markers',
          name: 'Nível Cozedor',
          marker: { color: 'green' },
        },
        {
          x: tempo,
          y: pressaoCozedor,
          type: 'scatter',
          mode: 'lines+markers',
          name: 'Pressão Cozedor',
          marker: { color: 'purple' },
        },
        {
          x: tempo,
          y: capacitanciaCozedor,
          type: 'scatter',
          mode: 'lines+markers',
          name: 'Capacitância Cozedor',
          marker: { color: 'orange' },
        },
        {
          x: tempo,
          y: aberturaValvulaAlimentacao,
          type: 'scatter',
          mode: 'lines+markers',
          name: 'Abertura Válvula Alimentação',
          marker: { color: 'yellow' },
        },
      ]}
      layout={{
        title: titleOfChart,
        xaxis: { title: 'Tempo' },
        yaxis: { title: 'Temperatura' },
      }}
    />
  );
}

export default MultijatoChart;
