import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Typography } from '@mui/material';
import MultijatoChart from './components/MultiJatoChart';
import Grid from '@mui/material/Grid2';
import Paper from '@mui/material/Paper';

interface MultijatoData {
  tempo: string;
  temperatura_entrada_multijato: number;
  temperatura_saida_multijato: number;

  abertura_valvula_alimentacao: number;
  nivel_cozedor: number;
  capacitancia_cozedor: number;
  pressao_cozedor: number;

  abertura_valvula_alimentacao_0: number;
  nivel_cozedor_0: number;
  capacitancia_cozedor_0: number;
  pressao_cozedor_0: number;

  abertura_valvula_alimentacao_1: number;
  nivel_cozedor_1: number;
  capacitancia_cozedor_1: number;
  pressao_cozedor_1: number;

  abertura_valvula_alimentacao_2: number;
  nivel_cozedor_2: number;
  capacitancia_cozedor_2: number;
  pressao_cozedor_2: number;

  abertura_valvula_alimentacao_3: number;
  nivel_cozedor_3: number;
  capacitancia_cozedor_3: number;
  pressao_cozedor_3: number;

  abertura_valvula_alimentacao_4: number;
  nivel_cozedor_4: number;
  capacitancia_cozedor_4: number;
  pressao_cozedor_4: number;

  abertura_valvula_alimentacao_5: number;
  nivel_cozedor_5: number;
  capacitancia_cozedor_5: number;
  pressao_cozedor_5: number;

  abertura_valvula_alimentacao_6: number;
  nivel_cozedor_6: number;
  capacitancia_cozedor_6: number;
  pressao_cozedor_6: number;

  abertura_valvula_alimentacao_7: number;
  nivel_cozedor_7: number;
  capacitancia_cozedor_7: number;
  pressao_cozedor_7: number;
}

function MultijatoDashboard() {
  const [data, setData] = useState<MultijatoData[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get<MultijatoData[]>('http://127.0.0.1:8000/multijato/');
        setData(response.data);
        setLoading(false);
      } catch (err) {
        setError('Erro ao buscar dados da API');
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (error) {
    return <Typography color="error">{error}</Typography>;
  }

  if (loading) {
    return <Typography>Carregando...</Typography>;
  }

  const tempo = data.map((item) => item.tempo);
  const temperaturaEntrada = data.map((item) => item.temperatura_entrada_multijato);
  const temperaturaSaida = data.map((item) => item.temperatura_saida_multijato);

  const aberturaValvulaAlimentacao = data.map((item) => item.abertura_valvula_alimentacao);
  const nivelCozedor = data.map((item) => item.nivel_cozedor);
  const capacitanciaCozedor = data.map((item) => item.capacitancia_cozedor);
  const pressaoCozedor = data.map((item) => item.pressao_cozedor);

  const aberturaValvulaAlimentacao0 = data.map((item) => item.abertura_valvula_alimentacao_0);
  const nivelCozedor0 = data.map((item) => item.nivel_cozedor_0);
  const capacitanciaCozedor0 = data.map((item) => item.capacitancia_cozedor_0);
  const pressaoCozedor0 = data.map((item) => item.pressao_cozedor_0);

  const aberturaValvulaAlimentacao1 = data.map((item) => item.abertura_valvula_alimentacao_1);
  const nivelCozedor1 = data.map((item) => item.nivel_cozedor_1);
  const capacitanciaCozedor1 = data.map((item) => item.capacitancia_cozedor_1);
  const pressaoCozedor1 = data.map((item) => item.pressao_cozedor_1);

  const aberturaValvulaAlimentacao2 = data.map((item) => item.abertura_valvula_alimentacao_2);
  const nivelCozedor2 = data.map((item) => item.nivel_cozedor_2);
  const capacitanciaCozedor2 = data.map((item) => item.capacitancia_cozedor_2);
  const pressaoCozedor2 = data.map((item) => item.pressao_cozedor_2);

  const aberturaValvulaAlimentacao3 = data.map((item) => item.abertura_valvula_alimentacao_3);
  const nivelCozedor3 = data.map((item) => item.nivel_cozedor_3);
  const capacitanciaCozedor3 = data.map((item) => item.capacitancia_cozedor_3);
  const pressaoCozedor3 = data.map((item) => item.pressao_cozedor_3);

  const aberturaValvulaAlimentacao4 = data.map((item) => item.abertura_valvula_alimentacao_4);
  const nivelCozedor4 = data.map((item) => item.nivel_cozedor_4);
  const capacitanciaCozedor4 = data.map((item) => item.capacitancia_cozedor_4);
  const pressaoCozedor4 = data.map((item) => item.pressao_cozedor_4);

  const aberturaValvulaAlimentacao5 = data.map((item) => item.abertura_valvula_alimentacao_5);
  const nivelCozedor5 = data.map((item) => item.nivel_cozedor_5);
  const capacitanciaCozedor5 = data.map((item) => item.capacitancia_cozedor_5);
  const pressaoCozedor5 = data.map((item) => item.pressao_cozedor_5);

  const aberturaValvulaAlimentacao6 = data.map((item) => item.abertura_valvula_alimentacao_6);
  const nivelCozedor6 = data.map((item) => item.nivel_cozedor_6);
  const capacitanciaCozedor6 = data.map((item) => item.capacitancia_cozedor_6);
  const pressaoCozedor6 = data.map((item) => item.pressao_cozedor_6);

  return (
    <Container maxWidth="lg">
      <Typography variant="h4" gutterBottom>
        Dashboard Multijato
      </Typography>
      <Grid container spacing={2}>
        <Grid size={{ xs: 12, md: 10, lg: 8 }}>
          <Paper elevation={2} style={{ padding: '8px' }}>
            <MultijatoChart
              tempo={tempo}
              temperaturaEntrada={temperaturaEntrada}
              temperaturaSaida={temperaturaSaida}
              aberturaValvulaAlimentacao={aberturaValvulaAlimentacao}
              nivelCozedor={nivelCozedor}
              capacitanciaCozedor={capacitanciaCozedor}
              pressaoCozedor={pressaoCozedor}
              titleOfChart={'Dados Multijato 1'}
            />
          </Paper>
        </Grid>
        <Grid size={{ xs: 12, md: 10, lg: 8 }}>
          <Paper elevation={2} style={{ padding: '8px' }}>
            <MultijatoChart
              tempo={tempo}
              temperaturaEntrada={temperaturaEntrada}
              temperaturaSaida={temperaturaSaida}
              aberturaValvulaAlimentacao={aberturaValvulaAlimentacao0}
              nivelCozedor={nivelCozedor0}
              capacitanciaCozedor={capacitanciaCozedor0}
              pressaoCozedor={pressaoCozedor0}
              titleOfChart={'Dados Multijato 2'}
            />
          </Paper>
        </Grid>

        <Grid size={{ xs: 12, md: 10, lg: 8 }}>
          <Paper elevation={2} style={{ padding: '8px' }}>
            <MultijatoChart
              tempo={tempo}
              temperaturaEntrada={temperaturaEntrada}
              temperaturaSaida={temperaturaSaida}
              aberturaValvulaAlimentacao={aberturaValvulaAlimentacao1}
              nivelCozedor={nivelCozedor1}
              capacitanciaCozedor={capacitanciaCozedor1}
              pressaoCozedor={pressaoCozedor1}
              titleOfChart={'Dados Multijato 3'}
            />
          </Paper>
        </Grid>

        <Grid size={{ xs: 12, md: 10, lg: 8 }}>
          <Paper elevation={2} style={{ padding: '8px' }}>
            <MultijatoChart
              tempo={tempo}
              temperaturaEntrada={temperaturaEntrada}
              temperaturaSaida={temperaturaSaida}
              aberturaValvulaAlimentacao={aberturaValvulaAlimentacao2}
              nivelCozedor={nivelCozedor2}
              capacitanciaCozedor={capacitanciaCozedor2}
              pressaoCozedor={pressaoCozedor2}
              titleOfChart={'Dados Multijato 4'}
            />
          </Paper>
        </Grid>

        <Grid size={{ xs: 12, md: 10, lg: 8 }}>
          <Paper elevation={2} style={{ padding: '8px' }}>
            <MultijatoChart
              tempo={tempo}
              temperaturaEntrada={temperaturaEntrada}
              temperaturaSaida={temperaturaSaida}
              aberturaValvulaAlimentacao={aberturaValvulaAlimentacao3}
              nivelCozedor={nivelCozedor3}
              capacitanciaCozedor={capacitanciaCozedor3}
              pressaoCozedor={pressaoCozedor3}
              titleOfChart={'Dados Multijato 5'}
            />
          </Paper>
        </Grid>

        <Grid size={{ xs: 12, md: 10, lg: 8 }}>
          <Paper elevation={2} style={{ padding: '8px' }}>
            <MultijatoChart
              tempo={tempo}
              temperaturaEntrada={temperaturaEntrada}
              temperaturaSaida={temperaturaSaida}
              aberturaValvulaAlimentacao={aberturaValvulaAlimentacao4}
              nivelCozedor={nivelCozedor4}
              capacitanciaCozedor={capacitanciaCozedor4}
              pressaoCozedor={pressaoCozedor4}
              titleOfChart={'Dados Multijato 6'}
            />
          </Paper>
        </Grid>

        <Grid size={{ xs: 12, md: 10, lg: 8 }}>
          <Paper elevation={2} style={{ padding: '8px' }}>
            <MultijatoChart
              tempo={tempo}
              temperaturaEntrada={temperaturaEntrada}
              temperaturaSaida={temperaturaSaida}
              aberturaValvulaAlimentacao={aberturaValvulaAlimentacao5}
              nivelCozedor={nivelCozedor5}
              capacitanciaCozedor={capacitanciaCozedor5}
              pressaoCozedor={pressaoCozedor5}
              titleOfChart={'Dados Multijato 7'}
            />
          </Paper>
        </Grid>

        <Grid size={{ xs: 12, md: 10, lg: 8 }}>
          <Paper elevation={2} style={{ padding: '8px' }}>
            <MultijatoChart
              tempo={tempo}
              temperaturaEntrada={temperaturaEntrada}
              temperaturaSaida={temperaturaSaida}
              aberturaValvulaAlimentacao={aberturaValvulaAlimentacao6}
              nivelCozedor={nivelCozedor6}
              capacitanciaCozedor={capacitanciaCozedor6}
              pressaoCozedor={pressaoCozedor6}
              titleOfChart={'Dados Multijato 8'}
            />
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
}

export default MultijatoDashboard;
