/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class CrmDashboard extends Component {
    setup() {
        this.state = useState({
            kpi: {},
            chart: [],
            activity: [],
            funnel: [],
            date_from: null,
            date_to: null,
        });

        // ✅ ใช้ ORM (ถูกต้องใน Odoo 19)
        this.orm = useService("orm");

        onWillStart(() => this.loadData());
    }

    async loadData() {
        const data = await this.orm.call(
            "crm.dashboard",
            "get_all",
            [],
            {}
        );

        this.state.kpi = data.kpi;
        this.state.chart = data.chart;
        this.state.activity = data.activity;
        this.state.funnel = data.funnel;

        this.renderChart();
    }

    renderChart() {
        const ctx = document.getElementById("lineChart");
        if (!ctx) return;

        // 🔥 กัน chart ซ้อน
        if (this.chartInstance) {
            this.chartInstance.destroy();
        }

        this.chartInstance = new Chart(ctx, {
            type: 'line',
            data: {
                labels: this.state.chart.map(c => c.date),
                datasets: [
                    {
                        label: 'Leads',
                        data: this.state.chart.map(c => c.total),
                    },
                    {
                        label: 'Won',
                        data: this.state.chart.map(c => c.won),
                    }
                ]
            }
        });
    }
}

CrmDashboard.template = "crm_dashboard_template";
registry.category("actions").add("crm_dashboard_tag", CrmDashboard);