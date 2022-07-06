import { makeStyles } from '@mui/styles';

const useStyles = makeStyles((theme) => ({
  titles: {
    marginTop: '5px',
    textAlign: 'left',
    fontFamily: '"Copse", serif',
    fontWeight: '400',
    fontSize: '15px',
    lineHeight: '14px'
  },
  sliderGrids: {
    marginTop: '15px'
  },
  firstSliderGrid: {
    marginTop: '25px'
  },
  tooltipsText: {
    fontSize: '14px'
  },
  tooltips: {
    marginLeft: '5px'
  },
  formControl: {
    "& .MuiInputBase-root": {
      color: "#6EC177",
      borderColor: "#6EC177",
      borderWidth: "1px",
      borderStyle: "solid",
      borderRadius: "100px",
      minWidth: "120px",
      justifyContent: "center"
    },
    "& .MuiSelect-select.MuiSelect-select": {
      paddingRight: "0px"
    }
  },
  select: {
    width: "auto",
    fontSize: "12px",
    "&:focus": {
      backgroundColor: "transparent"
    }
  },
  selectIcon: {
    position: "relative",
    color: "#6EC177",
    fontSize: "14px"
  },
  paper: {
    borderRadius: 12
  },
  list: {
    paddingTop: 0,
    paddingBottom: 0,
    "& li": {
      fontWeight: 200,
      paddingTop: 8,
      paddingBottom: 8,
      fontSize: "12px"
    },
    "& li.Mui-selected": {
      color: "white",
      background: "#6EC177"
    },
    "& li.Mui-selected:hover": {
      background: "#6EC177"
    }
  }
}));

export default useStyles;
