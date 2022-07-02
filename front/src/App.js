import './App.css';
import BeerForm from "./components/BeerForm"
import BeerInfo from "./components/BeerInfo"

import { Box, Grid, CircularProgress } from '@mui/material';
import { getBeerInfo } from './services/beerExpertService';
import { useState } from 'react';
import useStyles from './styles';

function App() {
  const classes = useStyles();

  const [beerInfo, setBeerInfo] = useState();
  const [loading, setLoading] = useState(false);

  const fetchBeer = async (input) => {
    setLoading(true);
    const response = await getBeerInfo(input)
    if (response.ok) {
      setBeerInfo(response.data)
      console.log(response.data)
    }

    setLoading(false)
  }

  return (
    <Box className="App">
      <h2 className="center">Master Brew</h2>
      <BeerForm getBeerInfo={fetchBeer} />

      { loading && 
        <Grid container className={classes.gridContainer}>
          <Grid item xs={12} className={classes.gridProgress}>
            <CircularProgress /> 
          </Grid>
        </Grid>
      }

      {beerInfo && (
        <BeerInfo info={beerInfo} />
      )}
    </Box>

  );
}

export default App;
