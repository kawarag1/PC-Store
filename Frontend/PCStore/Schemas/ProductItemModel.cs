using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PCStore.Schemas
{
    public class ProductItemModel
    {
        public int Id {  get; set; }

        public string Name { get; set; }

        public double Cost { get; set; }

        public int Counter { get; set; }

        public string ImageUrl { get; set; }

        public string Article { get; set; }

    }
}
