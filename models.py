# -*- coding: utf-8 -*-

from openerp import models, fields, api

class candidat(models.Model):
	_name='recrutement.candidat'
    #_inherit="hr.employee" 
	_description="Informations du Candidat"

	situation=fields.Selection(string="Situation",selection=[('Nouveau','Nouveau'),('RDV Thechnique','RDV Technique'),('RDV RH','RDV RH'),('Disqualifie','Disqualifie'),('Annulation','Annulationn'),('Recrut sur mission','Recrut sur mission'),('Proposition faite','Proposition faite'),('Contrat signe','Contrat signe')])
	fonction=fields.Selection(string="Fonctions", selection=[('Consultant','Consultant'),('CP','CP'),('IED','IED')])
	mobilite=fields.Selection(string="Mobilité", selection=[('local','Local'),('Region','Region'),('Pays','Pays'),('Continent','Continent'),('Monde','Monde')])
	date_disp=fields.Date(string="Disponibilité",)
	permet_cond=fields.Selection(string="Permet de conduite", selection=[('Aucun','Aucun'),('Categorie A','Categorie A'),('Categorie B','Categorie B')])
	contrat=fields.Selection(string="Type de contrat", selection=[('CDD','CDD'),('CDI','CDI'),('CDI de chantier','CDI de chantier'),('Interim','Interim'),("Contrat d'apprentissage",u"Contrat d'apprentissage"),('Contrat de professionnalisation','Contrat de professionnalisation'),('Convention de stage','Convention de stage'),('Freelance','Freelance')])
	domaine_ids=fields.One2many(comodel_name='recrutement.domaine', inverse_name='id_cand', string='Domaines')
	langue_ids=fields.One2many(comodel_name='recrutement.langue', inverse_name='id_cand', string='Langues')
	logiciel_ids=fields.One2many(comodel_name='recrutement.logiciel', inverse_name='id_cand', string='Logiciels')
	langage_ids=fields.One2many(comodel_name='recrutement.langage_prog', inverse_name='id_cand', string='Langages de Programmation')
	
	
class domaine(models.Model):
	_name='recrutement.domaine'
	_description="cette classe contient les differents domaines"
	
	nom=fields.Char(string="Domaine", size=50, required=True)
	annee_exp=fields.Integer(string="Année d'experience")
	niveau=fields.Selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')])
	id_cand=fields.Many2one(comodel_name='recrutement.candidat', string='candidat', ondelete='cascade')
	
	#_sql_constraints =[('unique_nom','unique(nom)','ce domaine existe deja ! ')]

	
class logiciel(models.Model):
	_name='recrutement.logiciel'
	_description='cette classe contient les differents type de logiciels'
	
	nom=fields.Char(string="Logiciel", size=50, required=True)
	niveau=fields.Selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')])
	id_cand=fields.Many2one(comodel_name='recrutement.candidat', string='candidat', ondelete='cascade')
	
	


class langue(models.Model):
	_name='recrutement.langue'
	_description='cette classe contient les differentes langues'
	
	nom=fields.Char(string="Langue", size=50, required=True)
	niveau=fields.Selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')])
	id_cand=fields.Many2one(comodel_name='recrutement.candidat', string='candidat', ondelete='cascade')
	
	

class langage_prog(models.Model):
	_name='recrutement.langage_prog'
	_description='cette classe contient les differents types de langage de programmation'
	
	
	nom=fields.Char(string="langage de programmation", size=50, required=True)
	niveau=fields.Selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')])
	id_cand=fields.Many2one(comodel_name='recrutement.candidat', string='candidat', ondelete='cascade')
	
	

class cvtheque(models.Model):
	_name='recrutement.cvtheque'
	_description='cette classe contient les liens vers les CV'
	
	nom=fields.Char(string="CV", size=50, required=True)
	niveau=fields.Selection(string="Niveau", selection=[('Theorie','Theorie'),('Connaissances','Connaissances'),('Pratique','Pratique'),('Maitrise','Maitrise'),('Expert','Expert')])
	id_cand=fields.Many2one(comodel_name='recrutement.candidat', string='candidat', ondelete='cascade')
	
