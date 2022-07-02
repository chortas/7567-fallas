import React, { useState } from 'react';
import { Card, Grid, Button, Typography } from '@mui/material';
import InputSlider from '../InputSlider';
import CategoricInput from '../CategoricInput';
import useStyles from './styles';

const OPTIONS = ["Muy poco", "Poco", "Regular", "Mucho", "Todo"]

export default function SimulateRulesForm({getBeerInfo}) {
  const classes = useStyles();

  const [initialGravity, setInitialGravity] = useState("Regular"); //palabra
  const [finalGravity, setFinalGravity] = useState("Regular"); // palabra
  const [color, setColor] = useState(); //numero
  const [alcoholGraduation, setAlcoholGraduation] = useState(); //numero
  const [bitterness, setBitterness] = useState(); //numero

  const handleColor = (event, newValue) => {
    setColor(parseInt(newValue));
  }

  const handleBitternes = (event, newValue) => {
    setBitterness(parseInt(newValue));
  }

  const handleAlcoholGraduation = (event, newValue) => {
    setAlcoholGraduation(parseInt(newValue));
  }

  const handleConfirm = () => {
    const input = {
      initial_gravity: initialGravity,
      final_gravity: finalGravity,
      color,
      bitterness,
      alcohol_graduation: alcoholGraduation,
    }
    getBeerInfo(input);
  }

  return (
    <Card sx={{ marginLeft: 10, marginRight: 10, padding: 5 }}>
        <Typography gutterBottom variant="h6" component="div">
        Definí las caracteristicas de la cerveza
          </Typography>
    <Grid container>
      <CategoricInput 
        options={OPTIONS}
        title={"Gravedad Original"}
        tooltip={"Gravedad específica de la cerveza medida antes de la fermentación (OG)"}
        value={initialGravity}
        handleValueChange={setInitialGravity}
      />

      <CategoricInput 
        options={OPTIONS}
        title={"Gravedad Final"}
        tooltip={"Gravedad específica de la cerveza medida luego de la fermentación (GF)"}
        value={finalGravity}
        handleValueChange={setFinalGravity}
      />

      <InputSlider 
        max={45}
        title={"Color"}
        tooltip={"Rango de color que tiene la cerveza (SRM)"}
        value={color}
        handleValueChange={handleColor}
      />

      <InputSlider 
        max={100}
        title={"Amargura"}
        tooltip={"Porcentaje de alcohol tiene la cerveza en base a su volumen total (%)"}
        value={bitterness}
        handleValueChange={handleBitternes}
      />

      <InputSlider 
        max={15}
        title={"Graduación Alcohólica"}
        tooltip={"Grado de amargor teórico que posee la cerveza (IBU)"}
        value={alcoholGraduation}
        handleValueChange={handleAlcoholGraduation}
      />


    </Grid>
    <Grid item xs={24}>

    <Grid item xs={12} className={classes.buttonsGrid}>
        <Button onClick={handleConfirm} color="primary">
          Obtener cerveza
        </Button>
      </Grid>

  </Grid>
  </Card>
  );
}
