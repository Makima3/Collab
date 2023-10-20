import React from 'react'
import style from '../styleMed.module.css' 
export const  Medicine = () => {
  return (
<div className= {style.Service}>
  <div className={style.Block}>
    <button className={style.InfoServices}>Лікування</button>
    </div> 
    <div className={style.Block}>
    <button className={style.InfoServices}>Хірургічні процедури</button>

    </div>
    <div className={style.Block}>
    <button className={style.InfoServices}>Лабораторна діагностика</button>

    </div>
    <div className={style.Block}>
    <button className={style.InfoServices}>Візуальна діагностика</button>

    </div>
    <div className={style.Block}>
    <button className={style.InfoServices}>Стоматолія</button>

    </div>

    <div className={style.Block}>
    <button className={style.InfoServices}>Дерматологія</button>

    </div>
  </div>  )
}
