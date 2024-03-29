import React from 'react';
import { Grid, Select, MenuItem, Tooltip } from '@mui/material';
import HelpIcon from '@mui/icons-material/Help';
import useStyles from './styles';



export default function CategoricInput({options, title, tooltip, value, handleValueChange, step=1, titleSize=6, sliderSize=6}) {
  const classes = useStyles();

  const handleChange = (event) => {
    handleValueChange(event.target.value);
  };

  return (
    <>
      <Grid className={classes.firstSliderGrid} item xs={titleSize} style={{paddingTop: '18px'}}>
        <Grid container className={classes.titles}>
            <div style={{marginTop: '3px'}}>
                {title}
            </div>
          <Tooltip className={classes.tooltips} placement="right" title={<span className={classes.tooltipsText}>{tooltip}</span>}>
            <HelpIcon color="action" fontSize="small"></HelpIcon>
          </Tooltip>
        </Grid>
      </Grid>
      <Grid className={classes.firstSliderGrid} item xs={sliderSize}  style={{paddingTop: '18px', paddingBottom: '18px'}}>
      <Select
          labelId="demo-simple-select-helper-label"
          id="demo-simple-select-helper"
          value={value}
          label=""
          onChange={handleChange}
        >
            {options.map(opt => (
                <MenuItem key={opt} value={opt}>{opt}</MenuItem>
            ))}
        </Select>
      </Grid>
    </>
  );
}
