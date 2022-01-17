using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ChristMath_7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Main();
            Draw();
        }
        private void Main()
        {
            double
                a = 2, b = 4, // [1, 3]
                x, 
                h,
                np = 1000, // произвольный выбор количества шагов для показа инфы  
                nx = 10, // кол-во шагов сетки
                e = 0.0001;
            double[] F = new double[2];

            // Метод Явная схема 1-го порядка (Эйлера)
            for (h = (b - a) / nx, x = a; ; x = a, nx *=2, h /= 2)
            {
                double[] y = new double[2] { 2 * a, Math.Exp(a) };

                if (np != 0) Out(x, y, h); //вывод инфы через кол-во шагов
                else np = nx + 1;

                for(int n = 0; n <= nx; n++, x += h)
                {
                    FPR(x, y, ref F);

                    for(int j=0; j<y.Length;j++)
                    {
                        y[j] += h * F[j];
                    }
                     if(n%np == 0) Out(x, y, h);
                }
                double de = Math.Abs(Math.Exp(x) - y[1]);
                if (de <= e)
                {
                    Out(x, y, h); break;
                }
                
            }
        }
        private void Draw()
        {
            double
               a = 2, b = 4, // [1, 3]
               x = a,
               nx = 10, // кол-во шагов сетки
               h = (b - a) / nx;
            double[] F = new double[2];
            double[] y = new double[2] { 2 * a, Math.Exp(a) };
           

            // Метод Явная схема 1-го порядка (Эйлера)
            for (int n = 0; n <= nx; n++, x += h)
            {
                FPR(x, y, ref F);
                for (int j = 0; j < y.Length; j++)
                {
                    y[j] += h * F[j];
                }
              

                //chart1.Series[0].Points.AddXY(x, 2*x);
                //chart1.Series[0].Points[n].Color = Color.Red;

                //chart1.Series[1].Points.AddXY(x, Math.Exp(x));
                //chart1.Series[1].Points[n].Color = Color.Green;

                chart2.Series[0].Points.AddXY(x, y[0]);
                chart2.Series[0].Points[n].Color = Color.Red;

                chart2.Series[1].Points.AddXY(x, y[1]);
                chart2.Series[1].Points[n].Color = Color.Green;
            }
        }
        private void FPR(double x, double[] y, ref double[] F) // рассчет функций по значениям из метода М1 
        {
            F[0] = (2*y[0])+(y[1]+Math.Exp(x))/Math.Exp(x) - 4*x;
            F[1] = (2*x*y[1]) / y[0]; 
        }
        private void Out(double x, double[] y, double h)
        {
            Console.WriteLine("x = "+ x + "\t h = " + h +
                "\ny1 = " + y[0] + "\tU1 = "+ 2 * x + "\td1 = "+ (2*x-y[0])+
                "\ny2 = "+ y[1] + "\tU2 = " + Math.Exp(x) + "\td2 = " + (Math.Exp(x) - y[1]) + "\n");
        }

        private void chart1_Click(object sender, EventArgs e)
        {

        }

    }
}
