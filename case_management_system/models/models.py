# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CaseManagementSystem(models.Model):
    _name = 'case.case'
    _description = 'Case Management System'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'
    
    name = fields.Char(string='Name', default='New', required=True)
    state = fields.Selection([('apply', 'Apply'), ('pre_qualification', 'Pre-qualification'), ('qualified', 'Qualified'), ('rejected', 'Rejected')], string='State', required=True, default='apply')
    # Applicant Information
    contact_name = fields.Char(string='Contact Name', required=True)
    contact_email = fields.Char(string='Contact Email', required=True)
    contact_phone = fields.Char(string='Contact Phone', required=True)
    contact_age = fields.Integer(string='Contact Age', required=True)
    project_name = fields.Char(string='Project Name', required=True)
    project_description = fields.Text(string='Project Description', required=True)
    # General Information & Idea Description 
    business_nature = fields.Text(string='Business Nature', required=False)
    sector_category = fields.Char(string='Sector Category', required=False)
    business_registration_type = fields.Text(string='Business Registration Type', required=False)
    problems_to_be_solved = fields.Text(string='Problems to be Solved', required=False)
    offered_services = fields.Text(string='Offered Services', required=False)
    competitive_advantage = fields.Text(string='Competitive Advantage', required=False)
    target_audience = fields.Text(string='Target Audience', required=False)
    challenges = fields.Text(string='Challenges', required=False)
    business_model = fields.Text(string='Business Model', required=False)
    profit_model = fields.Text(string='Profit Model', required=False)
    previous_investments = fields.Text(string='Previous Investments', required=False)
    
    # Operational History & Funding Requirements
    business_start_date = fields.Date(string='Business Start Date', required=False)
    
    # Funding Requirements
    funding_amount = fields.Float(string='Funding Amount', required=False)
    company_registration_date = fields.Date(string='Company Registration Date', required=False)
    
    # Upload Documents
    is_business_plan = fields.Boolean(string='Is Business Plan', default=False)
    business_plan = fields.Binary(string='Business Plan')
    
    is_general_info = fields.Boolean(string='Is General Info', default=False)
    general_info = fields.Binary(string='General Info')
    
    is_pitch_deck = fields.Boolean(string='Is Pitch Deck', default=False)
    pitch_deck = fields.Binary(string='Pitch Deck')
    
    @api.model_create_multi
    def create(self, vals_list):
        env_sequence = self.env['ir.sequence']
        for val in vals_list:
            if val.get('name', 'New') == 'New':
                val['name'] = env_sequence.next_by_code('case.case.sequence')
        return super(CaseManagementSystem, self).create(vals_list)
